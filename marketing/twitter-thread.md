# Twitter / X launch thread

> Post as a single thread from @optimajet (or personal account if more
> reach). 9 tweets. Pin to profile until +200 likes. Repost manually 48h
> later from secondary account.

---

## Tweet 1 — hook

```
Spent the weekend turning screenshots into React forms.

Drop a screenshot of any form into Claude or Cursor → get back a
production-ready React form with validated JSON schema.

Free, MIT, no SaaS lock-in. Built on top of FormEngine.

How it works ↓

[ATTACH GIF: screenshot → form rendering — 8 seconds]
```

## Tweet 2 — problem

```
LLMs can already write JSX for forms. The problem is what they emit:

— random `style={{}}` everywhere
— hallucinated component names (RsForm? doesn't exist)
— half-validation, no a11y
— locked to whatever the LLM wrote that one time

You can't edit it visually. Your designer can't open it.
```

## Tweet 3 — the unlock

```
The fix: don't generate JSX. Generate schema.

FormEngine renders forms from a JSON schema:

{
  "type": "RsInput",
  "props": { "label": { "value": "Email" } },
  "schema": { "validations": [{ "key": "email" }] }
}

Schema is data. Data is editable, portable, validatable.
```

## Tweet 4 — what it produces

```
The skill produces 4 things every time:

1. form.json (FormEngine schema, validated)
2. App.tsx (12 lines, runs out of the box)
3. Validation report (Screen root ✓, unique keys ✓, layout-only css ✓)
4. Link to free Online FormBuilder so your designer can edit visually

Round-trip works. No vendor lock.
```

## Tweet 5 — the validator

```
Why a validator?

LLMs make the SAME 30+ mistakes generating forms:
— `RsTextarea` (no, capital A)
— `"label": "Email"` (must be wrapped: `{ value: "Email" }`)
— minLength validation (doesn't exist — use min with args.limit)
— smuggled <h2> in content strings

scripts/validate_schema.py catches all of them.
```

## Tweet 6 — install (3 ways)

```
Three ways to install:

🤖 Claude Code skill:
git clone https://github.com/optimajet/ai-form-builder ~/.claude/skills/ai-form-builder

📝 Cursor rule:
curl raw.../.cursor/rules/formengine.mdc -o .cursor/rules/formengine.mdc

🌊 Windsurf rule:
similar curl, .windsurf/rules/

MCP server: roadmap, help wanted.
```

## Tweet 7 — examples

```
4 reference examples in the repo:

— Signup with side-by-side name fields + TOS checkbox
— Contact form with min-length validation
— Multi-step onboarding (RsWizard, 3 steps)
— Survey with conditional fields (renderWhen + validateWhen)

Every one passes the validator. CI runs on every PR.
```

## Tweet 8 — competitive

```
This is for developers, not no-code users.

If you want a hosted form: use Tally / Typeform.
If you want to own React code that fits your design system: this.

Renders through RSuite, Material UI, or Mantine — pick the one your
app already uses. Same schema, three themes.
```

## Tweet 9 — CTA

```
⭐ Star: https://github.com/optimajet/ai-form-builder
⭐ Star FormEngine Core: https://github.com/optimajet/formengine

Drop a screenshot of any form in the replies and I'll generate the
schema for you live.

What forms are you tired of writing?
```

---

## Variations / alternates

**Alt hook (more aggressive):**
> Stop writing form code. Drop a screenshot, get a React form.
> Free, MIT, runs as a Claude Skill / Cursor rule.

**Alt hook (developer-pain framing):**
> "Make me a contact form" — every LLM, gives you 80 lines of JSX no
> one will ever maintain.
> Here's a skill that gives you JSON schema + 12 lines of App.tsx
> instead. The schema is portable, validated, round-trips through a
> visual editor.

## Posting checklist

- [ ] GIF attached to tweet 1 (8 seconds, screenshot → form)
- [ ] First reply tags @rauchg @t3dotgg @theo — relevant React-builder
  voices likely to retweet
- [ ] Pin to profile
- [ ] Repost to /r/reactjs after thread has 50+ likes (NOT before — empty
  Reddit threads die)
- [ ] Schedule LinkedIn version 24h later (different audience)
