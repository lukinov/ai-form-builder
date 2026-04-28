---
title: "From screenshot to React form in 30 seconds: an AI form builder for developers"
description: "Generate production-ready React forms from a screenshot, PDF, or text prompt — as a Claude Skill, Cursor Rule, or MCP server. Free, MIT, no vendor lock."
canonical_url: https://formengine.io/blog/ai-form-builder-react-claude-skill-cursor-rule
slug: ai-form-builder-react-claude-skill-cursor-rule
tags: [react, ai-form-builder, claude-skill, cursor-rules, formengine, json-schema-form, react-form-builder]
target_keywords:
  primary: "ai form builder for react"
  secondary: ["react form builder", "claude skill", "cursor rules", "react json schema form"]
---

# From screenshot to React form in 30 seconds: an AI form builder for developers

You've seen the no-code AI form builders — Tally, Typeform, Jotform, Fillout. Type "make me a contact form" into a chat, get back a hosted form. Embed it. Done.

It's a great workflow if you're not a developer.

If you _are_ a developer and your form has to live inside your React app, talk to your auth, hit your typed API, match your design system, validate with the rules your backend already uses, and ship to the same CI/CD as the rest of your code — those tools fall apart. You end up with an iframe, an upsell to "Designer Pro," and a form your designer can't edit anymore.

This post is about a different shape of AI form builder: one that targets **React developers**, outputs **portable JSON schema + real React code**, and runs as a **[Claude Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills), [Cursor Rule](https://cursor.com/docs/rules), or MCP server**.

It's MIT, it's free, and you can install it in 60 seconds.

## TL;DR

- Drop a screenshot, PDF, HTML, or plain-English description into Claude Code, Cursor, or Windsurf.
- Get back a `form.json` (FormEngine schema) and a runnable `App.tsx`.
- Schema is portable — paste into the [free Online FormBuilder](https://formbuilder.formengine.io) to drag-and-drop edit, ship to your CMS, localize, hand to a designer.
- Validates against a real list of component types — no hallucinated `RsForm` or `MtTextField`.
- Repo: <https://github.com/optimajet/ai-form-builder>. ⭐ if you find it useful.

## The problem with letting an LLM "just write a form"

Try this in any chat assistant: _"give me a React signup form with name, email, password, and a TOS checkbox."_

You'll get back ~80 lines of JSX. It probably renders. It's also probably:

- **Stylistically random** — `style={{ marginBottom: 12 }}` here, a `className="form-group"` there, a custom `<Input>` somewhere — none of which exist in your design system.
- **Half-validated** — `required` on some fields, regex on others, no `email` type, no min length on the password.
- **Not editable by anyone but the LLM** — the moment you want to add a field, you're back in chat re-prompting. Designers can't open it. Schema doesn't exist.
- **Locked to a one-shot output** — you can't serve it from a CMS, can't localize it, can't round-trip through a visual editor.

This is the gap "AI form builder" search results don't fill. The top 10 are all SaaS no-code tools. None of them generate **React code you own** with a **schema you can edit visually**.

## The schema-first approach

[FormEngine](https://github.com/optimajet/formengine) is a React form library with a different philosophy: **the form is data, not code**. You describe the form as a JSON schema and a `<FormViewer>` component renders it through one of three popular UI libraries — RSuite, Material UI, or Mantine.

```json
{
  "type": "Screen",
  "key": "signup",
  "children": [
    {
      "type": "RsInput",
      "key": "email",
      "props": { "label": { "value": "Email" }, "type": { "value": "email" } },
      "schema": { "validations": [{ "key": "required" }, { "key": "email" }] }
    }
  ]
}
```

That's a real form. Pass it to `<FormViewer>` and you have email validation, accessibility, theming, and everything else for free.

The schema:

- **Round-trips** through the [Online FormBuilder](https://formbuilder.formengine.io) — paste in, drag fields, paste out. No code regen.
- **Themes at the library level** — same JSON renders through whichever library matches your design system.
- **Lives in your repo** as a `.json` file you can serve from a CMS or localize.

This shape is exactly what an LLM should output. **Plain data is easier to validate than JSX**, and a real schema unlocks every workflow downstream.

## Enter the AI form builder

[`optimajet/ai-form-builder`](https://github.com/optimajet/ai-form-builder) is a small, open-source skill — really just a structured prompt plus a Python validator — that turns natural-language descriptions, screenshots, PDFs, or HTML into a valid FormEngine schema and a runnable `App.tsx`.

It ships in **four shapes**:

1. A **Claude Skill** for Claude Code / Cowork (drop into `~/.claude/skills/`)
2. A **Claude Code plugin** (one-line `/plugin install`)
3. A **Cursor rule** (`.cursor/rules/formengine.mdc`)
4. A **Windsurf rule**

(An MCP server is on the [roadmap](https://github.com/optimajet/ai-form-builder/tree/main/mcp-server) — looking for contributors.)

### What "validated" actually means

Here's why "schema-first" is the unlock for AI generation. The skill ships with [`scripts/validate_schema.py`](https://github.com/optimajet/ai-form-builder/blob/main/skills/ai-form-builder/scripts/validate_schema.py) which catches the 30+ ways an LLM tries to be clever:

- **Wrong type names** — `RsForm`, `RsSelectPicker`, `MtTextField`, `RsTextarea` (no, `RsTextArea` with capital A) — these are the exact mistakes LLMs make all the time. The validator has the canonical type list and rejects anything not in it.
- **Unwrapped prop values** — `"label": "Email"` instead of `"label": { "value": "Email" }`. Trips every LLM at first; the validator catches it instantly.
- **HTML smuggled into prop strings** — `<h2>Section</h2>` inside a `content` field, `<strong>` around a label, a sneaky `<br>`. All forbidden. Express structure with components (`RsCard` + `header`, `RsHeader`, `RsDivider`), not markup.
- **Visual styling in `css`** — `color`, `background`, `border`, `font-size`. The validator allows only layout properties (flex, grid, box-model). Visual styling goes in the UI library's theme provider, not the schema.
- **Bad validation rule keys** — `minLength` doesn't exist in FormEngine. It's `min` with `args.limit`. The validator has the full Zod set and rejects anything else.

Every example in the repo passes the validator. CI runs the validator on every PR. If you're contributing, you can't merge a broken schema.

## A 60-second tour

### 1. Install the skill (Claude Code)

```bash
git clone https://github.com/optimajet/ai-form-builder \
  ~/.claude/skills/ai-form-builder
```

Restart Claude Code. The skill auto-loads when you mention forms.

### 2. Ask for a form

> _"Build me a multi-step onboarding form: step 1 = email + password, step 2 = company name + industry dropdown, step 3 = notification preferences."_

### 3. Get back a real schema

The skill produces a `form.json` with `RsWizard` + three `RsWizardStep` children, validated, and an `App.tsx` that renders it. No companion CSS, no inline styles in the schema, validations on the right components.

### 4. Run it

```bash
npm install @react-form-builder/core @react-form-builder/components-rsuite rsuite
npm run dev
```

You have a working multi-step onboarding form. Type the data, watch validations fire, switch steps.

### 5. Edit it visually (optional)

Paste the contents of `form.json` into the [Online FormBuilder](https://formbuilder.formengine.io) → Import. You'll get a drag-and-drop editor on top of the same schema. Fix labels, reorder fields, add a field, paste back.

## How this compares to alternatives

| | This skill | react-hook-form | RJSF | Tally / Typeform |
|---|---|---|---|---|
| AI generation from screenshot | ✅ | ❌ | ❌ | partial |
| Validated JSON schema | ✅ | ❌ | ✅ | proprietary |
| Visual editor round-trip | ✅ | ❌ | ❌ | ✅ (their UI only) |
| You own the React code | ✅ | ✅ | ✅ | ❌ embed only |
| MIT, free | ✅ | ✅ | ✅ | ❌ |
| Theme via your design system | ✅ | ✅ | partial | limited |
| Multi-step wizards | ✅ | manual | manual | ✅ |
| Conditional rendering | ✅ | manual | partial | ✅ |

**vs. raw LLM output (no skill):** the skill catches 30+ failure modes a raw prompt won't. Schema is portable, App.tsx is themeable, no inline styles leaking in.

**vs. RJSF:** RJSF is great if you already have a JSON Schema (e.g., from an OpenAPI spec). It doesn't generate one for you. Different tool.

**vs. Tally / Typeform:** they're for non-developers. You can't own the React code. You can't ship to a CMS. You're paying per submission past the free tier.

## What it doesn't do (yet)

- No MCP server yet. [Roadmap](https://github.com/optimajet/ai-form-builder/tree/main/mcp-server) — when shipped, any IDE/API can call `generate_form`.
- No Chakra / Ant Design adapters yet. [Help wanted](https://github.com/optimajet/ai-form-builder/labels/help%20wanted).
- No automatic transform to React Hook Form runtime. Possible, not built.
- It will not pixel-match a scanned paper form. The schema captures **data**; visual fidelity is a theme-level concern.

## How to play with it right now

```bash
# Option 1 — Claude Code skill
git clone https://github.com/optimajet/ai-form-builder \
  ~/.claude/skills/ai-form-builder

# Option 2 — Cursor rule
mkdir -p .cursor/rules
curl -L https://raw.githubusercontent.com/optimajet/ai-form-builder/main/.cursor/rules/formengine.mdc \
  -o .cursor/rules/formengine.mdc

# Option 3 — Windsurf rule
mkdir -p .windsurf/rules
curl -L https://raw.githubusercontent.com/optimajet/ai-form-builder/main/.windsurf/rules/formengine.md \
  -o .windsurf/rules/formengine.md
```

Then describe a form. Or drop a screenshot of a form you've been meaning to digitize. The skill handles all four input shapes — text, image, PDF, HTML.

## Why we built this

FormEngine has been around for a few years. The schema-first approach is the right approach, but typing JSON by hand isn't fun. With LLMs that can read screenshots, the friction drops to near-zero — but only if the model knows what valid output looks like. That's what the skill is: a tight prompt with hard rules, a real validator, and four reference examples to calibrate.

If this saves you an afternoon, ⭐ the [skill repo](https://github.com/optimajet/ai-form-builder) and ⭐ [FormEngine Core](https://github.com/optimajet/formengine). It helps more developers find the MIT renderer.

If you find a regression — the skill emitted something the validator missed, or a real form that the validator wrongly rejected — open an issue. PRs welcome on examples, on the validator, on the MCP server, on additional UI library adapters.

---

**Repo:** <https://github.com/optimajet/ai-form-builder>  
**FormEngine Core:** <https://github.com/optimajet/formengine>  
**Free Online FormBuilder:** <https://formbuilder.formengine.io>  
**Docs:** <https://formengine.io/documentation/formengine-core/>
