#!/usr/bin/env python3
"""
FormEngine schema validator.

Validates a generated FormEngine JSON schema against the rules enforced by
the ai-form-builder skill:

  - Root must be a `Screen` component
  - Every component has `key` (unique), `type`, and (usually) `props`
  - All component types are members of the canonical type list per library
  - Every prop value is wrapped: {"value": ...} (or one of the other
    canonical wrappers — {"jsCode": ...}, {"action": ...}, etc.)
  - All validation rule keys exist in the FormEngine Zod set
  - No legacy `style` field anywhere
  - `css` / `wrapperCss` keys are LAYOUT-ONLY (no color/font/background/
    border/shadow/radius/opacity/transform/etc.)
  - No HTML markup smuggled into any prop string (no tags, no style=,
    no class= / className=, no <style>/<script> blocks)

Usage:
    python validate_schema.py path/to/form.json
    python validate_schema.py path/to/form.json --library mui
    python validate_schema.py - < form.json     # read from stdin

Exit codes:
    0  no errors (warnings are OK)
    1  errors found
    2  bad input / unreadable file
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from typing import Any, Iterable

# ---------------------------------------------------------------------------
# Canonical component type tables (subset — extend as @react-form-builder
# adds components). Keep in sync with references/component-types.md.
# ---------------------------------------------------------------------------

RSUITE_TYPES = {
    "Screen", "RsContainer", "RsCard", "RsHeader", "RsDivider", "RsStaticContent",
    "RsInput", "RsTextArea", "RsNumberFormat", "RsDatePicker", "RsDateRangePicker",
    "RsCheckbox", "RsCheckboxGroup", "RsRadioGroup", "RsToggle",
    "RsDropdown", "RsTagPicker", "RsCheckPicker", "RsCascader",
    "RsUploader", "RsRate", "RsSlider", "RsRangeSlider", "RsButton",
    "RsTooltip", "RsErrorMessage", "RsWizard", "RsWizardStep",
    "RsAutoComplete", "RsInputMask", "RsTimePicker", "RsColorPicker",
    "RsAvatar", "RsBreadcrumb", "RsTable", "RsList",
}

MUI_TYPES = {
    "Screen", "MuiBox", "MuiCard", "MuiTypography", "MuiDivider", "MuiStaticContent",
    "MuiTextField", "MuiSelect", "MuiAutocomplete", "MuiCheckbox", "MuiRadioGroup",
    "MuiSwitch", "MuiSlider", "MuiRating", "MuiDatePicker", "MuiTimePicker",
    "MuiDateTimePicker", "MuiButton", "MuiIconButton", "MuiTooltip",
    "MuiErrorWrapper", "MuiStepper", "MuiStep",
}

MANTINE_TYPES = {
    "Screen", "MtContainer", "MtCard", "MtTitle", "MtText", "MtDivider", "MtStaticContent",
    "MtTextInput", "MtTextarea", "MtPasswordInput", "MtNumberInput", "MtJsonInput",
    "MtSelect", "MtMultiSelect", "MtAutocomplete", "MtCheckbox", "MtCheckboxGroup",
    "MtRadioGroup", "MtSwitch", "MtSlider", "MtRangeSlider", "MtRating",
    "MtDatePicker", "MtDateTimePicker", "MtMonthPicker", "MtYearPicker", "MtTimeInput",
    "MtColorPicker", "MtColorInput", "MtFileInput", "MtSegmentedControl",
    "MtButton", "MtTooltip", "MtErrorWrapper", "MtStepper", "MtStepperStep",
}

LIBRARY_TYPES = {
    "rsuite": RSUITE_TYPES,
    "mui": MUI_TYPES,
    "mantine": MANTINE_TYPES,
}

# Common renames the skill should never emit. Map of wrong -> correct.
COMMON_TYPO_MAP = {
    "Form": "Screen",
    "RsForm": "RsCard or RsContainer",
    "RsSelectPicker": "RsDropdown",
    "RsRadio": "RsRadioGroup",
    "RsTextarea": "RsTextArea",
    "RsInputNumber": "RsNumberFormat",
    "RsUpload": "RsUploader",
    "MtDatePickerSingle": "MtDatePicker",
    "MtTextField": "MtTextInput",  # MUI name leaking into Mantine
}

# ---------------------------------------------------------------------------
# Validation rule keys (FormEngine Zod set)
# ---------------------------------------------------------------------------

VALID_VALIDATION_KEYS = {
    "required", "nonEmpty",
    "min", "max", "length",
    "email", "url", "uuid", "ip", "datetime",
    "regex", "includes", "startsWith", "endsWith",
    "lessThan", "moreThan", "integer", "multipleOf",
    "truthy", "falsy",
}

# ---------------------------------------------------------------------------
# CSS / wrapperCss layout-only allowlist
# ---------------------------------------------------------------------------

# Properties allowed in css / wrapperCss (layout only).
LAYOUT_KEY_PATTERN = re.compile(
    r"^("
    r"display|position|top|right|bottom|left|inset|inset(Block|Inline)(Start|End)?|zIndex|order|"
    r"overflow.*|boxSizing|"
    r"width|minWidth|maxWidth|height|minHeight|maxHeight|"
    r"margin.*|padding.*|"
    r"gap|rowGap|columnGap|"
    r"flex.*|alignItems|alignContent|alignSelf|justifyContent|justifyItems|justifySelf|placeItems|placeContent|placeSelf|"
    r"grid.*|aspectRatio"
    r")$"
)

# Visual-styling keys that must NOT appear in css / wrapperCss
VISUAL_KEY_PATTERN = re.compile(
    r"^("
    r"color|background.*|"
    r"border.*|boxShadow|borderRadius|"
    r"font.*|text.*|letterSpacing|lineHeight|"
    r"opacity|transform|filter|backdropFilter|"
    r"outline.*|cursor|pointerEvents|userSelect|"
    r"transition.*|animation.*"
    r")$"
)

# ---------------------------------------------------------------------------
# HTML markup detector (any tag, plus style=/class=/className= attributes)
# ---------------------------------------------------------------------------

HTML_TAG_RE = re.compile(r"<\s*/?\s*[a-zA-Z][a-zA-Z0-9-]*\b[^>]*>")
HTML_ATTR_RE = re.compile(r"""(?:^|[\s'"])(style|class|className)\s*=""", re.IGNORECASE)
STYLE_BLOCK_RE = re.compile(r"<\s*(style|script)\b[^>]*>", re.IGNORECASE)


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

@dataclass
class Issue:
    severity: str  # "error" or "warning"
    path: str
    message: str

@dataclass
class Result:
    issues: list[Issue] = field(default_factory=list)

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "warning"]

    def err(self, path: str, msg: str) -> None:
        self.issues.append(Issue("error", path, msg))

    def warn(self, path: str, msg: str) -> None:
        self.issues.append(Issue("warning", path, msg))


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------

def detect_library(component_types: Iterable[str]) -> str:
    """Best-effort guess from prefixes."""
    types = [t for t in component_types if t and t != "Screen"]
    rs = sum(1 for t in types if t.startswith("Rs"))
    mu = sum(1 for t in types if t.startswith("Mui"))
    mt = sum(1 for t in types if t.startswith("Mt"))
    if rs >= mu and rs >= mt:
        return "rsuite"
    if mu >= mt:
        return "mui"
    return "mantine"


def collect_types(node: Any, out: list[str]) -> None:
    if isinstance(node, dict):
        if isinstance(node.get("type"), str):
            out.append(node["type"])
        for v in node.values():
            collect_types(v, out)
    elif isinstance(node, list):
        for v in node:
            collect_types(v, out)


def is_wrapped_value(v: Any) -> bool:
    """A canonical FormEngine prop value is an object with one of these keys."""
    if not isinstance(v, dict):
        return False
    return any(k in v for k in ("value", "jsCode", "action", "expression", "code"))


def check_string_for_html(s: str, path: str, result: Result) -> None:
    if not isinstance(s, str) or not s:
        return
    if STYLE_BLOCK_RE.search(s):
        result.err(path, f"<style>/<script> block in prop string: {s[:60]!r}")
        return
    if HTML_TAG_RE.search(s):
        result.err(path, f"HTML tag in prop string (use components, not markup): {s[:80]!r}")
        return
    if HTML_ATTR_RE.search(s):
        result.err(path, f"style=/class=/className= attribute in prop string: {s[:80]!r}")


def check_css_object(css: Any, path: str, result: Result) -> None:
    """css / wrapperCss must be { any: { object: { layoutKey: value, ... } } }."""
    if css is None:
        return
    if isinstance(css, str):
        result.err(path, "css must be a nested object {any:{object:{...}}}, not a string")
        return
    if not isinstance(css, dict):
        result.err(path, "css must be an object")
        return

    # Walk into any.object if present; otherwise treat the dict as a flat keymap.
    inner = css
    if isinstance(css.get("any"), dict) and isinstance(css["any"].get("object"), dict):
        inner = css["any"]["object"]
    elif "any" in css and not isinstance(css.get("any"), dict):
        result.err(path, "css.any must be an object")
        return

    for key in inner.keys():
        if VISUAL_KEY_PATTERN.match(key):
            result.err(
                path,
                f"visual styling key '{key}' is forbidden in css/wrapperCss "
                f"(move to the UI library's theme provider)",
            )
        elif not LAYOUT_KEY_PATTERN.match(key):
            result.warn(
                path,
                f"unrecognised css key '{key}' (allowed = layout-only: flex/grid/box-model)",
            )


def walk(node: Any, path: str, result: Result, seen_keys: set[str], allowed_types: set[str]) -> None:
    if not isinstance(node, dict):
        return

    # Component nodes have a "type"
    if "type" in node and isinstance(node["type"], str):
        ctype = node["type"]
        # Type validity
        if ctype in COMMON_TYPO_MAP:
            result.err(path, f"unknown type '{ctype}' — use '{COMMON_TYPO_MAP[ctype]}' instead")
        elif ctype not in allowed_types:
            result.err(path, f"unknown type '{ctype}' for the selected library")

        # Key uniqueness
        key = node.get("key")
        if key is not None:
            if not isinstance(key, str) or not key:
                result.err(path, f"key must be a non-empty string (got {key!r})")
            elif key in seen_keys:
                result.err(path, f"duplicate key '{key}'")
            else:
                seen_keys.add(key)
        elif ctype != "Screen":
            result.warn(path, "component is missing 'key'")

        # Legacy 'style'
        if "style" in node:
            result.err(path, "legacy 'style' field is forbidden — use css/wrapperCss")

        # css / wrapperCss layout-only
        if "css" in node:
            check_css_object(node["css"], f"{path}.css", result)
        if "wrapperCss" in node:
            check_css_object(node["wrapperCss"], f"{path}.wrapperCss", result)

        # Props
        props = node.get("props")
        if props is not None:
            if not isinstance(props, dict):
                result.err(path, "props must be an object")
            else:
                for pname, pval in props.items():
                    ppath = f"{path}.props.{pname}"
                    if not is_wrapped_value(pval):
                        result.err(
                            ppath,
                            "prop value must be wrapped, e.g. {\"value\": ...} — never a bare value",
                        )
                    else:
                        # If wrapped with "value" and value is a string, scan for HTML
                        if isinstance(pval, dict) and isinstance(pval.get("value"), str):
                            check_string_for_html(pval["value"], ppath, result)

        # schema.validations
        schema = node.get("schema")
        if isinstance(schema, dict):
            validations = schema.get("validations")
            if validations is not None:
                if not isinstance(validations, list):
                    result.err(f"{path}.schema.validations", "validations must be an array")
                else:
                    for i, v in enumerate(validations):
                        vpath = f"{path}.schema.validations[{i}]"
                        if not isinstance(v, dict):
                            result.err(vpath, "validation entry must be an object")
                            continue
                        vkey = v.get("key")
                        if vkey not in VALID_VALIDATION_KEYS:
                            result.err(
                                vpath,
                                f"unknown validation key '{vkey}' "
                                f"(valid: {', '.join(sorted(VALID_VALIDATION_KEYS))})",
                            )

        # Recurse into children
        children = node.get("children")
        if isinstance(children, list):
            for i, ch in enumerate(children):
                walk(ch, f"{path}.children[{i}]", result, seen_keys, allowed_types)

    # Recurse into nested dict values that aren't components themselves
    for k, v in node.items():
        if k == "children":
            continue
        if isinstance(v, dict) and "type" in v:
            walk(v, f"{path}.{k}", result, seen_keys, allowed_types)


def validate(schema: dict, library: str | None = None) -> Result:
    result = Result()

    # Root invariants
    form = schema.get("form")
    if not isinstance(form, dict):
        result.err("$", "missing top-level 'form' object")
        return result

    root_type = form.get("type")
    if root_type != "Screen":
        result.err(
            "$.form.type",
            f"root type must be 'Screen' (got {root_type!r})",
        )

    # Library detection
    types_seen: list[str] = []
    collect_types(form, types_seen)
    detected = library or detect_library(types_seen)
    if detected not in LIBRARY_TYPES:
        result.warn("$", f"unknown library '{detected}' — defaulting to RSuite")
        detected = "rsuite"
    allowed = LIBRARY_TYPES[detected]

    walk(form, "$.form", result, seen_keys=set(), allowed_types=allowed)

    # Tooltip / error type sanity
    expected = {
        "rsuite":  ("RsTooltip",  "RsErrorMessage"),
        "mui":     ("MuiTooltip", "MuiErrorWrapper"),
        "mantine": ("MtTooltip",  "MtErrorWrapper"),
    }[detected]
    if "tooltipType" in schema and schema["tooltipType"] != expected[0]:
        result.warn("$.tooltipType", f"expected {expected[0]} for {detected}")
    if "errorType" in schema and schema["errorType"] != expected[1]:
        result.warn("$.errorType", f"expected {expected[1]} for {detected}")

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def format_report(result: Result, *, color: bool = True) -> str:
    if color and sys.stdout.isatty():
        RED, YEL, GRN, RST = "\033[31m", "\033[33m", "\033[32m", "\033[0m"
    else:
        RED = YEL = GRN = RST = ""
    lines = []
    for issue in result.issues:
        tag = f"{RED}error{RST}" if issue.severity == "error" else f"{YEL}warn{RST} "
        lines.append(f"  {tag}  {issue.path}: {issue.message}")
    if not result.errors and not result.warnings:
        lines.append(f"  {GRN}OK{RST}    schema is clean")
    elif not result.errors:
        lines.append(f"  {GRN}PASS{RST}  no errors ({len(result.warnings)} warning(s))")
    else:
        lines.append(f"  {RED}FAIL{RST}  {len(result.errors)} error(s), {len(result.warnings)} warning(s)")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Validate a FormEngine JSON schema")
    p.add_argument("path", help="path to form.json (or '-' for stdin)")
    p.add_argument(
        "--library",
        choices=["rsuite", "mui", "mantine"],
        help="target UI library (auto-detected if omitted)",
    )
    p.add_argument("--no-color", action="store_true")
    args = p.parse_args(argv)

    try:
        if args.path == "-":
            raw = sys.stdin.read()
        else:
            with open(args.path, encoding="utf-8") as f:
                raw = f.read()
        schema = json.loads(raw)
    except (OSError, json.JSONDecodeError) as e:
        print(f"could not read schema: {e}", file=sys.stderr)
        return 2

    result = validate(schema, library=args.library)
    print(format_report(result, color=not args.no_color))
    return 0 if not result.errors else 1


if __name__ == "__main__":
    sys.exit(main())
