# Product Hunt launch package

> Day-of-launch checklist + every piece of copy. Best launch day:
> Tuesday or Wednesday. Worst: Sunday/Monday (low traffic, hard to
> place top 5).

---

## Listing fields

### Name

```
AI Form Builder
```

(Generic-sounding but captures search; leave the brand attribution to
the tagline + maker.)

### Tagline (60 chars max)

```
Screenshot → React form. Claude Skill, Cursor Rule, MCP.
```

(Three-way positioning hook in 50 chars, lands the unique mechanism.)

Alt taglines to A/B in pre-launch:

- `From screenshot to validated React form in 30 seconds.` (54)
- `MIT AI form builder for React devs. No SaaS lock-in.` (52)

### Topic tags

`Developer Tools`, `Artificial Intelligence`, `Open Source`, `GitHub`

### First-comment description (maker post)

```
Hey Product Hunt 👋 I'm <name>, working on FormEngine — an
open-source React form library — for the past few years.

This week we're launching the AI half: a small, MIT-licensed
skill that turns screenshots, PDFs, HTML, or plain-English
descriptions into production-ready React forms with validated
JSON schema.

What's actually in the box:

🤖 Claude Skill (drop into ~/.claude/skills/)
📝 Cursor Rule (.cursor/rules/formengine.mdc)
🌊 Windsurf Rule
🔌 MCP server (roadmap, contributors welcome)

Why it's different from "just ask an LLM":

→ Output is portable JSON schema, not throwaway JSX
→ Schema round-trips through a free visual editor — your
  designer can edit it again
→ Real Python validator catches the 30+ failure modes LLMs hit
  (wrong component types, smuggled HTML, broken validations)
→ Renders through RSuite / MUI / Mantine — pick what your app
  uses

What it isn't:
- It's not a no-code SaaS. You own the React code.
- It won't pixel-replicate scanned paper forms.
- It doesn't generate JSX (that's the point).

Repo: https://github.com/optimajet/ai-form-builder

The skill, the renderer, and the visual editor are all MIT and
free. Built on top of FormEngine Core
(github.com/optimajet/formengine).

Drop a screenshot of any form in the comments and I'll generate
the schema for you live.

Thanks 🙏
```

### Gallery images (in order)

1. **Hero** — wide PNG (1270×760). Split: left = screenshot of a real
   form, right = JSON schema + tiny App.tsx, arrow between. Caption:
   "Screenshot → validated schema → React form"
2. **GIF** (≤3 MB) — same flow as the demo, animated, 8 seconds
3. **Comparison table** — vs. react-hook-form, RJSF, Tally — same as
   the README table, screenshot of it
4. **Validator output** — terminal screenshot showing a green checklist
   for one of the example schemas (proves "validated" is real)
5. **Three install snippets** — Claude / Cursor / Windsurf installs side
   by side

### Maker

`@<your-handle>` — list yourself. If FormEngine team has multiple, add
them as makers (collaborates on launch boost).

### Hunter

If reach is critical, ask a top hunter (e.g., Chris Messina —
@chrismessina) to hunt. Otherwise self-hunt is fine.

### Pricing model

`Free`

### Launch date

Pick a Tuesday 12:01 AM PT for max 24h ranking window. Tell every
contact 48h before the date so they can support on launch day, NOT
before (Product Hunt's algorithm penalizes early upvotes).

---

## Pre-launch (3–7 days before)

- [ ] Create the listing in **draft** mode, fill every field
- [ ] Share preview link with FormEngine team for review
- [ ] Schedule launch for Tuesday 12:01 AM PT
- [ ] Build a "ship list" — 30+ people you'll personally DM the
  launch link to on launch day
- [ ] Pre-write 5–10 reply-templates for predicted comments
  (pricing, vs. competitors, contributing)

## Launch day (Tuesday)

- [ ] 12:01 AM PT — verify listing is live
- [ ] 12:05 AM — post launch tweet (link to the PH page, NOT GitHub)
- [ ] 12:10 AM — post in any internal Slacks / dev community channels
  you're already in
- [ ] 8:00 AM PT — ship-list DMs go out (NOT before; PH penalizes
  pre-7am upvotes from new accounts)
- [ ] Reply to every comment within 30 min for the first 8 hours
- [ ] 6:00 PM PT — second wave of DMs to second-tier contacts
- [ ] Don't beg for upvotes. Don't say "please vote." Both auto-flag.

## Day after

- [ ] Thank everyone publicly via comment on the launch
- [ ] Post the final ranking + a screenshot to Twitter
- [ ] Send a "thanks" note to the top 5 commenters (they remember,
  they retweet next time)
