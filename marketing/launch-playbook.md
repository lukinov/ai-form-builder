# Launch playbook — day-by-day

> 2-week sequence. Each day is small enough to actually execute. The
> sequencing is deliberate — registries first (slow-acting, compound),
> then social spike, then HN/PH (need momentum from prior days).

---

## Pre-launch (T-7 to T-1)

### T-7 days — finalize artifacts

- [ ] Repo is public on `github.com/optimajet/ai-form-builder`
- [ ] All 4 example schemas validate (CI green)
- [ ] README hero image rendered (1270×760 PNG, screenshot → schema)
- [ ] Demo GIF recorded (8 seconds, ≤3 MB) — use [Kap](https://getkap.co)
  on macOS or [LICEcap](https://licecap.com) on Windows
- [ ] FormEngine team has reviewed every marketing doc

### T-5 days — repo polish

- [ ] **GitHub topics added** (use all 20):
  ```
  ai-form-builder, ai-form-generator, claude-skill, claude-code,
  claude-code-plugin, cursor-rules, cursorrules, windsurf, mcp,
  mcp-server, react, react-form-builder, react-forms,
  react-json-schema-form, react-hook-form, form-generator, formengine,
  json-schema-form, low-code, anthropic-skill
  ```
- [ ] Repo description set to:
  ```
  AI form builder for React — generate production-ready forms from a
  screenshot, PDF, HTML, or text prompt. Claude Skill / Cursor Rule /
  MCP server. MIT. Built on FormEngine Core.
  ```
- [ ] `.github/FUNDING.yml` points to optimajet
- [ ] CI is green on `main`
- [ ] First 5 issues created (good-first-issue labels): "Add Chakra
  adapter", "Port validator to TS for MCP", "Add KYC example", etc.

### T-3 days — Product Hunt prep

- [ ] PH listing created in DRAFT mode, scheduled for launch Tuesday
- [ ] Gallery images uploaded (5 total — see product-hunt.md)
- [ ] Maker page filled in (FormEngine team members)
- [ ] Hunter confirmed (or self-hunting)
- [ ] Ship-list of 30+ contacts compiled (NOT messaged yet)

### T-2 days — pre-warm the audience

- [ ] **Light Twitter teaser** from personal account: "Spent the
  weekend on something fun. Drops Tuesday." (NO link, NO details. Just
  a vague tease — primes followers to look for it.)
- [ ] DM 3–5 friends with engineering followings: ask them to retweet
  on Tuesday when the thread goes up. Give them the GIF preview.

### T-1 day (Sunday/Monday) — registry submissions

⚠️ **This is the highest-leverage day. Do these submissions BEFORE social.**

- [ ] PR to `PatrickJS/awesome-cursorrules` (DR 97, traffic 735)
- [ ] PR to `anthropics/skills` (THE registry)
- [ ] Submit to `cursor.directory` (DR 68, traffic 671)
- [ ] Submit to `cursorrules.org`
- [ ] Submit to `dotcursorrules.com`
- [ ] PR to `hesreallyhim/awesome-claude-code`
- [ ] Submit to `aitmpl.com/skills`

(Skip awesome-mcp-servers — wait until MCP actually ships.)

These take 1–14 days to merge. **Submitting on Monday means most are
visible on Tuesday/Wednesday — peak launch momentum.**

---

## Launch week

### Day 1 — Tuesday — Twitter + Product Hunt

**6:00 AM ET — Twitter thread goes live** (from @optimajet or personal
account, whichever has more relevant reach).

- [ ] 9 tweets, GIF on tweet 1 (see twitter-thread.md)
- [ ] Pin to profile
- [ ] Reply to every comment within 30 minutes for first 6 hours

**12:01 AM PT — Product Hunt listing goes live.**

- [ ] Verify it's live on Product Hunt
- [ ] Post launch tweet linking to the PH page (NOT the GitHub repo)
- [ ] First-comment maker post within 5 minutes of launch
- [ ] 8:00 AM PT — ship-list DMs go out (NOT before — PH algorithm
  penalizes early new-account upvotes)

**Throughout the day:**

- [ ] Reply to every PH comment within 30 minutes
- [ ] Quote-tweet anyone who shares your launch
- [ ] DO NOT explicitly ask for upvotes anywhere

### Day 2 — Wednesday — Show HN

**8:30 AM ET — Submit Show HN.**

- [ ] Title: `Show HN: AI Form Builder – screenshot to React form, as a Claude Skill or Cursor Rule`
- [ ] First comment within 60 seconds (see show-hn.md)
- [ ] Reply to every top-level comment within 30 minutes for 4 hours
- [ ] If it falls off the front page by 6pm, accept it. **Don't
  resubmit.** HN penalizes immediate resubmissions.

**Same day, 12:00 PM ET — Dev.to post goes live.**

- [ ] Set canonical URL to FormEngine blog version
- [ ] Tags: `react`, `ai`, `javascript`, `webdev`
- [ ] First-comment offer: "drop a form screenshot in the comments
  and I'll generate the schema live"

### Day 3 — Thursday — /r/reactjs

- [ ] Post to /r/reactjs (see reddit-posts.md)
- [ ] Reply to every comment within 60 minutes for first 6 hours
- [ ] If the post is removed by mods, message politely, don't
  resubmit

### Day 4 — Friday — /r/cursor

- [ ] Post to /r/cursor (Cursor-specific framing, see reddit-posts.md)

### Day 5 — Saturday — quiet day

- [ ] Don't post anything new
- [ ] Reply to anything still active from earlier in the week
- [ ] Track metrics: GitHub stars, repo traffic (Insights tab),
  Product Hunt rank, HN final placement

### Day 6 — Sunday — quiet

- [ ] Same as Saturday

### Day 7 — Sunday/Monday — /r/ClaudeAI

- [ ] Post to /r/ClaudeAI

---

## Week 2 — sustained content

### Day 8 — Tuesday — LinkedIn post

(Different audience than Twitter — typically engineering leads /
managers / decision-makers.)

- [ ] Post the LinkedIn version (see linkedin-post.md)
- [ ] First comment has the GitHub link (don't put it in the post body)

### Day 10 — Thursday — /r/webdev Showoff Saturday

(Wait for Showoff Saturday rather than posting on a non-showoff day —
risk of removal.)

- [ ] If Saturday is in this week, post then
- [ ] Otherwise wait for next Saturday

### Day 11 — Friday — second Twitter thread

If first thread did >200 likes, write a follow-up:
- "Things I learned shipping ai-form-builder this week" — the
  meta-post about lessons / surprises / numbers

If first thread was quiet, skip this.

### Day 14 — Monday — write blog #2

If traction is good, plan a second blog post targeting another
keyword from the Tier-3 long-tail (KD < 15):

- "React form validation with AI — how the schema makes it work" (KD
  2)
- "react-jsonschema-form alternatives in 2026" (KD 11)
- "Best React form library for AI-generated forms" (KD 0)

Each post links back to the repo + main blog post. SEO compounding.

---

## Tracking — what actually matters

| Metric | Day 1 target | Week 1 target | Month 1 target |
|---|---|---|---|
| GitHub stars | 50 | 250 | 800 |
| Repo views (unique) | 2 000 | 8 000 | 25 000 |
| HN front page time | — | 4+ hours | n/a |
| PH ranking | top 10 | top 20 | n/a |
| Twitter thread likes | 100 | 500 | 1 500 |
| `optimajet/formengine` star bump | +10 | +50 | +200 |
| `optimajet/formengine` traffic bump | +20% | +50% | +100% |

The last two rows are the actual point of this whole launch — the skill
is a top-of-funnel asset whose job is feeding traffic to FormEngine
Core. If the skill gets 800 stars and FormEngine Core picks up 200, the
launch worked.

---

## What to do if it flops

**HN fades fast (off front page in <2h):**
- Don't resubmit. Wait 6+ months.
- Post pivots to Reddit + Twitter. HN audience is one of many.

**PH ranks #15+:**
- Don't sweat it. PH-driven stars are nice but not the funnel.
- Focus on registry submissions getting merged (the slow-burn play).

**Reddit posts removed:**
- Message the mods, ask what specifically was the issue, don't
  resubmit until invited.
- Try a different sub the next week.

**Twitter thread <50 likes:**
- The framing didn't land. Save the thread, edit the hook, repost in
  3 weeks under a different angle ("things I learned…" works well as a
  re-spin)

---

## What success looks like at +30 days

- 800+ stars on `optimajet/ai-form-builder`
- Listed on at least 5 of the 7 Day-1 registries
- 1–2 organic Twitter mentions per week from devs who used it
- 1+ external blog post or video about it (write to the author of any
  such post — relationship is worth more than the inbound)
- FormEngine Core has +100–300 stars net from the skill traffic
- 3–5 GitHub issues from real users (not noise) that hint at v0.2
  priorities
