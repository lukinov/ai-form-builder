# Reddit launch posts

> Each subreddit has its own culture, mods, and rules. **Do not
> copy-paste the same post to all four.** Mods detect that and ban.
> Each version below is tailored.

---

## /r/reactjs — open-source release

**Subreddit rules:** No "self-promotion" without value. Mods enforce
strictly. Title must describe the tool, not sell it. Flair: "Resource"
or "Showoff Saturday" if launching on a Saturday.

**Title:**

```
[Open Source] AI Form Builder for React — generate forms from screenshots, output portable JSON schema
```

**Body:**

> Hey r/reactjs — I've been maintaining FormEngine (open-source React
> form library, MIT) for a while, and this weekend I packaged the AI
> generation half as a separate skill: drop a screenshot, PDF, or
> description into Claude Code / Cursor / Windsurf, get back a
> validated FormEngine schema and a runnable App.tsx.
>
> What makes it actually useful (vs. raw LLM JSX dumps):
>
> - Output is **schema**, not JSX — round-trips through a free visual
>   editor (https://formbuilder.formengine.io), portable to a CMS,
>   themeable at the library level.
> - **Real validator** — Python script that catches the 30+ failure
>   modes LLMs hit (wrong component types, smuggled HTML, broken
>   validation rule keys). CI runs on every PR.
> - Three install shapes: **Claude Skill**, **Cursor Rule**, **Windsurf
>   Rule**. MCP server on the roadmap.
> - Renders through RSuite / MUI / Mantine — pick what your app uses.
>
> Repo: https://github.com/optimajet/ai-form-builder
>
> Examples in the repo: signup, contact, multi-step onboarding (RsWizard),
> survey with conditional fields (renderWhen + validateWhen). Each one is
> a working `form.json` + `App.tsx`.
>
> Open to feedback on:
> - What forms are slowest in your codebase? (Want to add more
>   reference examples)
> - The MCP server — looking for contributors to port the validator to
>   TypeScript
> - The prompt itself — anything that's missing or wrong
>
> Both this skill and FormEngine Core are MIT.

---

## /r/webdev — broader audience, less React-specific

**Subreddit rules:** Self-promotion limited to "Showoff Saturday".
Otherwise post at risk.

**Best day:** Saturday (showoff thread)

**Title:**

```
[Showoff Saturday] AI Form Builder — turn a screenshot of any form into a validated React form
```

**Body:**

> Spent the week building a small open-source tool that turns
> screenshots of forms into production React code. Ships as a Claude
> Skill, a Cursor Rule, and a Windsurf Rule.
>
> Drop in a screenshot, PDF, HTML, or text description. Get back:
>
> 1. A validated JSON schema (FormEngine format)
> 2. A runnable App.tsx (12 lines)
> 3. Validation report
> 4. Link to a free visual editor where you can drag-and-drop edit the
>    same schema
>
> The schema is portable — same JSON renders through RSuite, MUI, or
> Mantine. Can be served from a CMS, localized, edited by a designer.
>
> Why schema instead of JSX? Schema is data. Data is editable,
> validatable, and round-trippable. JSX from an LLM is a one-shot
> output — nobody can edit it but the LLM that wrote it.
>
> MIT, free, no SaaS. https://github.com/optimajet/ai-form-builder
>
> Happy to answer questions or generate a schema for any form
> screenshot you drop in the comments.

---

## /r/ClaudeAI — community of skill / plugin enthusiasts

**Subreddit rules:** Anthropic-tool focused. No mod approval needed for
standard skill announcements.

**Title:**

```
New Claude Skill: AI Form Builder — generate React forms from screenshots
```

**Body:**

> Just published a Claude Skill that turns screenshots, PDFs, or text
> descriptions into production-ready React forms.
>
> Install:
>
> ```
> git clone https://github.com/optimajet/ai-form-builder \
>   ~/.claude/skills/ai-form-builder
> ```
>
> The skill produces a validated FormEngine JSON schema plus a
> runnable App.tsx. The schema is portable — opens in a free visual
> editor for drag-and-drop tweaks.
>
> What I learned building it:
>
> 1. **Validators are the secret sauce.** A skill prompt alone gets
>    you 70% there. The other 30% — wrong component type names,
>    unwrapped prop values, smuggled HTML in strings — needs a
>    deterministic check. Every output runs through
>    `scripts/validate_schema.py` before being shown to the user.
>
> 2. **Reference files matter.** SKILL.md is the entry point but the
>    skill loads `references/component-types.md` for the canonical
>    type list, `references/examples.md` to calibrate completeness, etc.
>    Saves a ton of tokens vs. inlining everything.
>
> 3. **Hard rules with examples.** "No HTML in prop strings" doesn't
>    work without "here's what to do instead" — `RsCard` with `header`
>    prop, `RsHeader` standalone, `RsDivider`. The skill spells out the
>    alternative for every forbidden pattern.
>
> Repo: https://github.com/optimajet/ai-form-builder
>
> Also packaged as a Cursor Rule and Windsurf Rule from the same
> source-of-truth SKILL.md, so you can use it outside Claude too.

---

## /r/cursor — Cursor-specific community

**Subreddit rules:** Cursor-specific tools and rules welcome.

**Title:**

```
New Cursor Rule: AI Form Builder for React — generate forms from screenshots
```

**Body:**

> Just released a Cursor rule that turns screenshots / PDFs / text
> descriptions into production React forms with validated JSON schema.
>
> Install:
>
> ```
> mkdir -p .cursor/rules
> curl -L https://raw.githubusercontent.com/optimajet/ai-form-builder/main/.cursor/rules/formengine.mdc \
>   -o .cursor/rules/formengine.mdc
> ```
>
> The rule auto-attaches when you edit `.tsx` / `.jsx` files
> containing form-related terms. Or invoke explicitly:
>
> > @formengine build me a multi-step onboarding form
>
> Output: `form.json` + `App.tsx`. The schema renders through FormEngine
> (RSuite / MUI / Mantine) and round-trips through the free visual
> builder at https://formbuilder.formengine.io.
>
> Repo: https://github.com/optimajet/ai-form-builder
>
> Also ships as a Claude Skill and Windsurf Rule.
>
> Both MIT, no SaaS.

---

## Posting cadence (CRITICAL — don't break)

**Day 1:** /r/reactjs (the hardest, most signal-rich)  
**Day 2:** /r/cursor (small, dedicated audience)  
**Day 3:** /r/ClaudeAI  
**Day 4–6:** wait — don't blast. Watch for organic traction.  
**Day 7 (Saturday):** /r/webdev Showoff Saturday

Mods cross-reference. Posting all four on day 1 = ban risk in at least
two of the four subs.

## Reply discipline

For all four:
- Reply to every comment within 60 minutes for the first 6 hours
- If someone reports a bug — fix it within 24h, reply with the commit
- Never argue with mods. If a post is removed, message politely, fix
  the cited issue, resubmit only if invited.
