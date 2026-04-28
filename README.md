# ai-form-builder

**AI Form Builder for React.** Generate production-ready React forms from a screenshot, PDF, HTML, or text prompt — as a Claude Skill, Cursor Rule, or Windsurf Rule. Outputs portable JSON schema + runnable React code. Built on top of [FormEngine Core](https://github.com/optimajet/formengine) (MIT, free forever).

## What this is

Drop a screenshot, PDF, HTML snippet, or plain-text description of a form into Claude / Cursor / Windsurf — get back a valid FormEngine JSON schema plus a runnable `App.tsx` that renders it through `@react-form-builder/core`. Every output passes a real validator (no hallucinated component types, no smuggled HTML, no broken validations).

Three install targets, one source of truth:

| Where you work | Install as | Trigger |
|---|---|---|
| Claude Code / Cowork | Claude skill | "make me a signup form" / drop a screenshot |
| Claude Code (one-line) | Plugin | `/plugin install ai-form-builder` |
| Cursor | Cursor rule | mention "form" / "FormEngine" |
| Windsurf | Windsurf rule | same |
| Any IDE / API (planned) | MCP server | call `generate_form` tool |

## Quick start

```bash
# 1. Install the runtime
npm install @react-form-builder/core @react-form-builder/components-rsuite rsuite

# 2. Drop the AI Form Builder into your assistant of choice (see below)

# 3. Say something like:
#    "Build me a signup form with name, email, password, and TOS checkbox"
```

You'll get back a `form.json` and an `App.tsx`. Run `npm run dev` and the form is live.

## Install as a Claude Skill

```bash
git clone https://github.com/lukinov/ai-form-builder.git ~/.claude/skills/ai-form-builder
```

Or, if you keep skills inside a project:

```bash
git clone https://github.com/lukinov/ai-form-builder.git .claude/skills/ai-form-builder
```

Restart Claude Code. The skill auto-loads when you mention forms, signup, contact, onboarding, etc., or drop a form screenshot.

## Install as a Claude Code plugin

```bash
/plugin marketplace add lukinov/ai-form-builder
/plugin install ai-form-builder
```

## Install as a Cursor rule

```bash
mkdir -p .cursor/rules
curl -L https://raw.githubusercontent.com/lukinov/ai-form-builder/main/.cursor/rules/formengine.mdc \
  -o .cursor/rules/formengine.mdc
```

The rule auto-attaches when you edit `.tsx` / `.jsx` files containing the words *form*, *signup*, *contact*, etc. Or invoke explicitly:

> @formengine build me a multi-step onboarding form

## Install as a Windsurf rule

```bash
mkdir -p .windsurf/rules
curl -L https://raw.githubusercontent.com/lukinov/ai-form-builder/main/.windsurf/rules/formengine.md \
  -o .windsurf/rules/formengine.md
```

## How it works

The skill produces four artifacts every time:

1. **`form.json`** — a normalized FormEngine schema, validated against the real list of component types from [`@react-form-builder/components-rsuite`](https://www.npmjs.com/package/@react-form-builder/components-rsuite) (or MUI / Mantine).
2. **`App.tsx`** — minimal runnable React; theming via the library's provider, no companion CSS.
3. **A validation report** — what passed, what was fixed (Screen root, unique keys, valid validation rule keys, layout-only `css`, no smuggled HTML markup).
4. **Next steps** — install command, doc links, an "import to Online FormBuilder" link your teammate can use to edit visually.

The same JSON schema round-trips through the [Online FormBuilder](https://formbuilder.formengine.io) — paste it in, drag fields, paste back. No vendor lock.

## Examples

| Use case | Schema | Notes |
|---|---|---|
| Signup form with TOS, side-by-side name fields | [examples/signup](examples/signup/) | Password validation, `truthy` consent, flex container |
| Contact form with multi-line message | [examples/contact](examples/contact/) | `RsTextArea`, `min` length validation |
| Multi-step onboarding wizard | [examples/multi-step-onboarding](examples/multi-step-onboarding/) | `RsWizard` + `RsWizardStep` |
| Survey with conditional fields | [examples/survey-conditional](examples/survey-conditional/) | `renderWhen` + `validateWhen` |

Each example folder has a working `form.json` + `App.tsx` you can paste straight into a Vite/Next/CRA project.

## Why FormEngine + AI

If you've tried generating forms with raw LLMs, you know the pain:

- Bare JSX dumps that can't be edited visually
- "Form" libraries that hallucinate component names
- Inline `<style>` blocks that don't match your theme
- No validation, no a11y, no round-trip with a designer
- A new component every time → no schema you can serve from a CMS

This skill solves all of that by targeting **FormEngine's JSON schema format**, which is:

- **Portable.** Plain data — feed it to FormViewer in React, edit it in the [Online FormBuilder](https://formbuilder.formengine.io), serve it from your API, localize it.
- **Round-trippable.** Designer ↔ JSON ↔ Designer. No code regeneration.
- **Library-agnostic.** Same schema renders through RSuite, Material UI, or Mantine — pick the one your app already uses.
- **Validated.** A real Python validator (`scripts/validate_schema.py`) catches the 30+ failure modes LLMs hit (wrong types, unwrapped props, smuggled HTML, visual styling in `css`).

You're not paying for any of this. FormEngine Core is MIT and the skill is MIT.

## Vs. alternatives

| | This skill + FormEngine | react-hook-form | react-jsonschema-form (RJSF) | No-code SaaS (Tally, Typeform, Jotform) |
|---|---|---|---|---|
| AI generation from screenshot/PDF | yes | no | no | partial |
| Validated JSON schema | yes | no (just hooks) | yes | proprietary |
| Visual editor round-trip | yes (Online FormBuilder) | no | no | yes (their UI only) |
| You own the React code | yes | yes | yes | no, embed only |
| MIT license, free | yes | yes | yes | no |
| Theme-able with your design system | yes (RSuite/MUI/Mantine themes) | yes | partial | limited |
| Multi-step wizards | yes (`RsWizard`) | manual | manual | yes |
| Conditional rendering | yes (`renderWhen`) | manual | partial | yes |

## What the skill outputs (real example)

Input:

> Build me a signup form: name, email, password (8+ chars), and a TOS checkbox.

Output excerpt (`form.json`):

```json
{
  "form": {
    "type": "Screen",
    "key": "signup",
    "children": [
      {
        "type": "RsCard",
        "props": { "header": { "value": "Create your account" } },
        "children": [
          {
            "type": "RsInput",
            "key": "email",
            "props": { "label": { "value": "Email" }, "type": { "value": "email" } },
            "schema": { "validations": [{ "key": "required" }, { "key": "email" }] }
          },
          {
            "type": "RsInput",
            "key": "password",
            "props": { "label": { "value": "Password" }, "type": { "value": "password" } },
            "schema": {
              "validations": [
                { "key": "required" },
                { "key": "min", "args": { "limit": 8 } }
              ]
            }
          }
        ]
      }
    ]
  }
}
```

Plus a 12-line `App.tsx`. Run `npm run dev` and you have a working form.

## MCP server roadmap

A standalone Model Context Protocol server (`generate_form`, `validate_schema`, `list_components` tools) is on the roadmap — see [`mcp-server/README.md`](mcp-server/README.md). Star this repo to be notified.

## Repository layout

```
ai-form-builder/
├── skills/ai-form-builder/    # The skill source (SKILL.md + references + scripts)
├── .claude-plugin/            # Claude Code plugin manifest
├── .cursor/rules/             # Cursor .mdc rule
├── .windsurf/rules/           # Windsurf rule
├── mcp-server/                # MCP server (roadmap)
├── examples/                  # 4 reference outputs (signup/contact/multi-step/survey)
├── docs/                      # Long-form documentation
└── .github/                   # Workflows + issue templates
```

## FAQ

**Q: Does this work without Claude / Cursor?**
A: Today the skill needs an LLM host that loads it. The MCP server (in roadmap) will expose the same logic to any IDE or API client.

**Q: Do I need a FormEngine license to use this?**
A: No. FormEngine Core is MIT — runs in production, no fees. The commercial **FormEngine Designer** is optional for visual editing in your own app; the free **Online FormBuilder** is enough for most workflows.

**Q: Can I use this with Material UI / Mantine instead of RSuite?**
A: Yes. Tell the skill which library you want, or it'll auto-detect from the surrounding project. All three component libraries are supported.

**Q: My form has a custom field type. Will it still work?**
A: The skill maps to FormEngine's built-in component set (35+ in RSuite, ~25 each in MUI / Mantine). For custom field types, register them with FormEngine's component registry and add a note to the skill prompt — it'll pick them up.

**Q: How is this different from v0 / Vercel AI / shadcn-ui generators?**
A: Those generate JSX. We generate **schema** — portable data that round-trips through a visual editor, ships to a CMS, and renders through any of three component libraries.

**Q: Does this support React Hook Form / Zod / Yup?**
A: FormEngine has its own validation layer (Zod-equivalent rule keys). If you must use RHF, the schema can be transformed at runtime — see [docs/integration-with-rhf.md](docs/integration-with-rhf.md).

## Contributing

Issues and PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Especially looking for:

- Additional UI library adapters (Chakra, Ant Design)
- More example schemas (admin panels, KYC, surveys with branching)
- MCP server contributors

## License

MIT — see [LICENSE](LICENSE). Built on top of [FormEngine](https://github.com/optimajet/formengine) by Optimajet.

## Related projects

- [FormEngine Core](https://github.com/optimajet/formengine) — the renderer this skill targets
- [Online FormBuilder](https://formbuilder.formengine.io) — free visual editor, paste JSON in / out
- [FormEngine docs](https://formengine.io/documentation/formengine-core/) — full reference

---

If this saved you an afternoon, consider starring [FormEngine Core](https://github.com/optimajet/formengine) — it helps more developers find the MIT renderer.
