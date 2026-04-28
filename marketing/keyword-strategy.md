# Keyword & SERP strategy

Locked from Ahrefs research, US data, April 2026.

## Primary target keywords (where we play)

| Keyword | US vol | KD | Intent | Strategy |
|---|---|---|---|---|
| ai form builder | 500 | 34 | commercial ($5 CPC) | **Primary landing target.** Lane is empty for developer-focused angle. |
| ai form generator | 350 | 39 | branded info | Co-target, same content cluster. |
| react form builder | 150 | **8** | branded info | **Easy win.** FormEngine already ranks #9 — compound. |
| react json schema form | 150 | **11** | branded info | Indirect: "RJSF alternative" angle. |
| cursor rules | 4 900 | 37 | informational | **Distribution play.** Get into registries. |
| claude skill | 900 | 31 | branded info | **Distribution play.** PR to anthropics/skills. |
| claude code skill | 1 000 | — | informational | Same cluster. |
| claude code plugin | 900 | — | informational | Plugin packaging captures this. |

## Long-tail content cluster (KD < 20, easy ranks)

Each gets a dedicated blog post / docs page:

| Keyword | KD | Page |
|---|---|---|
| how to use ai form builder | 2 | tutorial: "How to use AI to build React forms" |
| react form validation | 2 | tutorial: "AI-generated React forms with validation" |
| react form library | 0 | listicle: "Best React form libraries in 2026" (FormEngine + alts) |
| react form validation best practices | 0 | guide |
| react native form | 0 | (FormEngine-mobile angle) |
| best ai form builder | 18 | comparison page |
| react login form | 8 | example/template page |
| react form example | 7 | examples page |
| low code form builder | 0 | positioning page |
| ai google form builder | 2 | comparison: "AI Google Forms alternative for React" |
| claude design skill | 16 | (related) |
| claude skill creator | 20 | (related) |

## Avoid head-on competition

| Keyword | Why we don't fight directly |
|---|---|
| react-hook-form (5 900 vol) | DR 76 incumbent; we're a different category (UI library + AI generation) |
| react-jsonschema-form / rjsf | DR 97 incumbent; route via "alternative" / "vs" pages |
| no code form builder (KD 74) | SaaS turf — Tally/Typeform — we're not no-code |

## SERP competitive intel

**"ai form builder" top 10:** all SaaS no-code (Tally, Jotform, Fillout, Feathery, Makeform). Position #1 = Google Workspace marketplace listing. Position #7 = simple listicle (DR 53). **No developer-targeted tool in top 10. Empty lane.**

**"react form builder" top 10:** react-hook-form's form-builder #1, coltorapps #2 with DR 19 (proves low-DR sites can rank), Reddit /r/reactjs threads #3, **@react-form-builder/core npm #4**, **formengine.io #9**. We have existing SEO equity to compound.

**"cursor rules" top 10:** half the page is registries — `cursor.directory` (DR 68), `cursorrules.org`, `dotcursorrules.com`, `PatrickJS/awesome-cursorrules`. **The registries ARE the distribution channel.**

**"claude skill" top 10:** `code.claude.com/docs/en/skills` #1, Reddit threads #2, **`github.com/anthropics/skills` #3** (the registry). Medium tutorials, aitmpl.com.

## Distribution priority list (Day 1)

Higher than blog content:

| Registry | DR / Reach | Action |
|---|---|---|
| github.com/PatrickJS/awesome-cursorrules | DR 97, 735 traffic | PR our `.cursor/rules/formengine.mdc` + listing entry |
| github.com/anthropics/skills | THE Anthropic registry | PR our skill pack |
| cursor.directory | DR 68, 671 traffic | submit via form |
| cursorrules.org | DR 23, 368 traffic | submit |
| dotcursorrules.com | DR 21, 294 traffic | submit |
| github.com/hesreallyhim/awesome-claude-code | community list | PR |
| github.com/punkpeye/awesome-mcp-servers | when MCP is shipped | PR |
| npm: `@formengine/ai-form-builder` (skill package) | npm SEO | publish stub |

## GitHub topics (use all 20)

Repo topics carry into GitHub search. Use:

```
ai-form-builder
ai-form-generator
claude-skill
claude-code
claude-code-plugin
cursor-rules
cursorrules
windsurf
mcp
mcp-server
react
react-form-builder
react-forms
react-json-schema-form
react-hook-form
form-generator
formengine
json-schema-form
low-code
anthropic-skill
```

## README H1 (locked)

> # AI Form Builder for React
> ### Generate production-ready React forms from a screenshot, PDF, HTML, or text prompt — as a Claude Skill, Cursor Rule, or MCP server. Outputs portable JSON schema + React code. MIT, free.

This single line targets:
- "ai form builder" (commercial, 500/mo)
- "react form builder" (KD 8, 150/mo)
- "claude skill" (informational, 900/mo)
- "cursor rule" (informational, 4 900/mo)
- "mcp server" (rising, ~500/mo)
