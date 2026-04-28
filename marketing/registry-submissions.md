# Registry submissions — Day 1 distribution package

> SERP analysis showed registries dominate the "cursor rules" / "claude
> skill" search results. Half the top 10 for "cursor rules" is
> registries (cursor.directory DR 68 / cursorrules.org / dotcursorrules
> / awesome-cursorrules). Getting listed = free traffic forever.

> **Submit on Day 1 of launch, before any social posts.** Registries
> are the slow-acting compounding distribution; social is the spike.

---

## Priority order

| # | Registry | DR / Reach | URL | Effort |
|---|---|---|---|---|
| 1 | PatrickJS/awesome-cursorrules | 97 / 735 traffic | https://github.com/PatrickJS/awesome-cursorrules | PR |
| 2 | anthropics/skills | THE registry | https://github.com/anthropics/skills | PR |
| 3 | cursor.directory | 68 / 671 traffic | https://cursor.directory | submit form |
| 4 | cursorrules.org | 23 / 368 traffic | https://cursorrules.org | submit |
| 5 | dotcursorrules.com | 21 / 294 traffic | https://dotcursorrules.com | submit |
| 6 | hesreallyhim/awesome-claude-code | community list | https://github.com/hesreallyhim/awesome-claude-code | PR |
| 7 | aitmpl.com/skills | curated list | https://www.aitmpl.com/skills/ | submit |
| 8 | punkpeye/awesome-mcp-servers | when MCP ships | https://github.com/punkpeye/awesome-mcp-servers | PR (later) |

---

## 1. awesome-cursorrules — PR

**Repo:** github.com/PatrickJS/awesome-cursorrules

**Branch name:** `add-formengine-react-rule`

**File to add:** `rules/react-formengine-cursorrules-prompt-file/.cursorrules`

(Replicate from `.cursor/rules/formengine.mdc` but rename to `.cursorrules`
since this list expects the legacy filename.)

**README entry to add (alphabetical):**

```markdown
- [React FormEngine — AI Form Builder](./rules/react-formengine-cursorrules-prompt-file)
```

**PR title:**

```
Add: React FormEngine AI Form Builder rule
```

**PR description:**

```markdown
Adds a Cursor rule that turns screenshots, PDFs, HTML, or text descriptions
into production-ready React forms with validated FormEngine JSON schema.

The rule covers:
- All FormEngine type names (35+ across RSuite/MUI/Mantine adapters)
- Hard schema rules (Screen root, wrapped prop values, layout-only css)
- Validation rule keys (Zod set: required, min, max, email, regex, etc.)
- Plain-text-only prop strings (no HTML markup smuggled in)
- Side-by-side fields, multi-step wizards, conditional rendering

Source repo: https://github.com/optimajet/ai-form-builder
```

---

## 2. anthropics/skills — PR

**Repo:** github.com/anthropics/skills

**Branch name:** `add-ai-form-builder`

**Folder structure (mirror their convention):**

```
skills/
└── ai-form-builder/
    ├── SKILL.md
    ├── references/
    │   ├── schema-anatomy.md
    │   ├── component-types.md
    │   ├── examples.md
    │   └── react-starter.md
    └── scripts/
        └── validate_schema.py
```

(Copy from our `skills/ai-form-builder/` verbatim.)

**README addition (or wherever they list community skills):**

```markdown
### ai-form-builder

Generate production-ready React forms from screenshots, PDFs, HTML, or text descriptions. Outputs portable [FormEngine](https://github.com/optimajet/formengine) JSON schema + runnable React code. Validator catches 30+ common LLM failure modes. MIT.

**Trigger phrases:** "make me a form", "build a signup form", "convert this form to React", drops a form screenshot/PDF.
```

**PR description:**

```markdown
Adds the `ai-form-builder` skill — converts natural-language descriptions, screenshots, PDFs, or HTML into validated FormEngine JSON schemas plus runnable React code.

What it does:
- Extracts form structure (fields, types, validations, sections, wizards) from any of 4 input types
- Emits a JSON schema validated against the canonical type list of `@react-form-builder/components-rsuite` / `components-material-ui` / `components-mantine`
- Emits a 12-line `App.tsx` that renders through `<FormViewer>` from `@react-form-builder/core`
- Reports validation results (Screen root, unique keys, layout-only css, no smuggled HTML, valid validation rule keys)

Includes a Python validator (`scripts/validate_schema.py`) that catches 30+ regressions including unknown types, unwrapped prop values, visual styling in `css`, HTML markup in prop strings, and invalid validation rule keys.

Source repo (with examples + tests): https://github.com/optimajet/ai-form-builder
```

---

## 3. cursor.directory — submit form

**URL:** https://cursor.directory/submit (or wherever their submission
flow lives — check on the day)

**Title:**
```
React + FormEngine — AI Form Builder
```

**Tags:** `react`, `forms`, `ai-form-builder`, `formengine`,
`json-schema`, `multi-step`

**Description (200–500 words):**
```
Generate production-ready React forms from screenshots, PDFs, HTML, or
plain-text descriptions. Output is a portable FormEngine JSON schema
plus a runnable App.tsx — the schema round-trips through a free
visual editor (formbuilder.formengine.io) so designers can edit
visually after generation.

The rule enforces all FormEngine schema invariants:
- Screen root (never "Form")
- Wrapped prop values ({ "value": "..." }, never bare strings)
- Layout-only css (flex/grid/box-model — no color/font/border)
- Plain-text prop strings (no HTML smuggled in)
- Validation keys from the FormEngine Zod set

Renders through RSuite (default), Material UI, or Mantine.

Repo: https://github.com/optimajet/ai-form-builder
```

**Rule file URL:**
```
https://raw.githubusercontent.com/optimajet/ai-form-builder/main/.cursor/rules/formengine.mdc
```

---

## 4. cursorrules.org — submit

**URL:** https://cursorrules.org/submit

Same description and tags as cursor.directory.

---

## 5. dotcursorrules.com — submit

**URL:** https://dotcursorrules.com/submit

Same description.

---

## 6. awesome-claude-code — PR

**Repo:** github.com/hesreallyhim/awesome-claude-code

**File:** README.md (add under "Skills" or "Community Skills" section)

**Entry:**

```markdown
- **[ai-form-builder](https://github.com/optimajet/ai-form-builder)** — Generate production-ready React forms from screenshots, PDFs, HTML, or text descriptions. Outputs validated [FormEngine](https://github.com/optimajet/formengine) JSON schema + runnable React code. Ships as a Claude Skill, Cursor Rule, and Windsurf Rule. MIT.
```

---

## 7. aitmpl.com/skills — submit

If they have a submission flow, use the same description as
cursor.directory above.

---

## 8. awesome-mcp-servers — PR (LATER, when MCP ships)

**Repo:** github.com/punkpeye/awesome-mcp-servers

**Section:** "Form Generation" (create if doesn't exist) or "Developer
Tools"

**Entry:**

```markdown
- **[FormEngine MCP](https://github.com/optimajet/ai-form-builder/tree/main/mcp-server)** — `generate_form`, `validate_schema`, `list_components` tools for AI-driven React form generation. Backed by FormEngine Core. MIT.
```

DO NOT submit this until the MCP server actually has a working
`npx @formengine/mcp-server` command. Submitting an empty stub gets the
PR rejected and burns goodwill.

---

## Submission discipline

- All PRs / submissions on Day 1 (Monday, before social launch on
  Tuesday)
- Use a clean GitHub account with at least 2 prior PRs to other
  repos (mods are wary of single-purpose accounts)
- Each PR has the proper conventions of the target repo (alphabetical
  ordering, lowercase tags, etc.)
- Do not submit the same project twice if rejected; respect maintainer
  decisions and ask what would unblock acceptance
