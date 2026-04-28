# Show HN submission

> HN rules: title ≤ 80 chars, no marketing fluff, no exclamation
> marks. First comment is the maker post — that's where the context
> goes. Best time: Tuesday or Wednesday, 8–10am ET. Avoid Mondays
> (catch-up day) and Friday/weekend (low traffic).

---

## Title (80 chars max — this fits at 79)

```
Show HN: AI Form Builder – screenshot to React form, as a Claude Skill or Cursor Rule
```

Alt titles to test:

- `Show HN: Generate React forms from screenshots, as a Claude Skill / Cursor Rule` (79)
- `Show HN: From screenshot to validated React form schema in 30 seconds` (66)

The first one wins because "Claude Skill" + "Cursor Rule" are HN-recognizable nouns right now.

## URL

```
https://github.com/optimajet/ai-form-builder
```

(Submit the GitHub repo, not the blog post. HN consistently ranks repos higher than blog posts for "Show HN".)

## First comment (post within 60 seconds of submission)

> Hey HN — author here.
>
> Quick context: we've maintained FormEngine, an open-source React
> form library, for a few years. The library renders forms from a JSON
> schema, but typing the schema by hand isn't fun. With LLMs that read
> screenshots well now, the friction can drop to near-zero — IF the
> model is told what valid output looks like.
>
> So this is the LLM half: a small skill (really just a structured
> prompt) plus a Python validator that catches the 30+ ways LLMs go
> wrong on form generation:
>
> — Wrong component types (`RsForm` doesn't exist; `RsTextarea` is
>   `RsTextArea` with a capital A; `MtTextField` is the MUI name leaking
>   into Mantine output)
> — Unwrapped prop values (`"label": "Email"` instead of
>   `{ "value": "Email" }`)
> — HTML smuggled into prop strings (`<h2>Section</h2>` inside a
>   `content` field — sneaky, breaks portability)
> — Visual styling in `css` (`color`, `border`, `font-size`) — those
>   belong in the UI library's theme provider, not the schema
> — Validation rule keys that don't exist (`minLength` isn't a thing —
>   it's `min` with `args.limit`)
>
> The validator catches all of these. CI runs it on every PR. Every
> example in the repo passes.
>
> What you get out: a `form.json` (FormEngine schema) and a runnable
> `App.tsx`. Schema is portable — paste into the free Online
> FormBuilder (https://formbuilder.formengine.io) to drag-and-drop edit,
> ship to your CMS, localize, hand to a designer.
>
> It ships in three shapes: Claude Skill, Cursor Rule, Windsurf Rule.
> An MCP server is on the roadmap — looking for contributors.
>
> The whole thing (skill + library) is MIT. We're not gating anything;
> the renderer is free, the visual editor is free.
>
> Open to feedback on the prompt, the validator, what to add to the
> example set, and what would unblock the MCP server.

## Anticipated objections + replies (have these ready)

**"This is just a prompt."**
> Yes — the prompt is half. The other half is the schema validator
> (`scripts/validate_schema.py`). Without the validator the LLM emits
> broken schemas regularly. With it, every output is checked against
> the real component-type list and the FormEngine validation rule set
> before the user sees it. The repo also has 4 reference examples that
> pass the validator and CI runs it on every PR.

**"Why FormEngine instead of react-hook-form?"**
> Different shape. RHF is a hooks library — you write the JSX. FormEngine
> is schema-first — you describe the form as data and a viewer renders
> it. The skill targets schema because schema round-trips through a
> visual editor, ships to a CMS, and stays themeable at the library
> provider level. RHF + AI generation just gives you JSX, which is
> back to the original problem.

**"How is this different from v0 / shadcn AI generators?"**
> Those generate JSX components. This generates **schema** + a thin
> render wrapper. Schema is editable visually after generation; JSX
> isn't (without re-prompting). Different output shape, different
> downstream workflow.

**"Why three install shapes? Pick one."**
> Different developers live in different tools. The skill is the same
> source-of-truth `SKILL.md`; the Cursor and Windsurf rules are
> shorter mirrors of the same hard rules. No duplication of intent.

**"Where's the MCP server?"**
> Scaffold + roadmap is in `mcp-server/`. Not shipped — port of the
> Python validator to TypeScript is the blocking work.
> [`help wanted`](https://github.com/optimajet/ai-form-builder/labels/help%20wanted)
> if anyone wants to take it.

**"This is a marketing channel for FormEngine."**
> Fair. FormEngine has been MIT and free for years; we want more
> people to know it exists. The skill is the same MIT, the Online
> FormBuilder is free, the renderer is free. There's no lead-gen funnel
> wrapped around this.

## Posting checklist

- [ ] Confirm HN account is at least 1 week old (newer accounts get
  shadow-suppressed)
- [ ] Submit at 8:30am ET on a Tuesday or Wednesday (not Monday — too
  much weekend backlog; not Thursday — Thursday afternoon is when HN
  pulls back)
- [ ] Post first comment within 60 seconds of submission
- [ ] DO NOT ask for upvotes anywhere — instant flag
- [ ] DO NOT submit the same URL twice within 24h
- [ ] Reply to every top-level comment within 30 minutes for the first
  4 hours — comment-engagement is a ranking signal
- [ ] If it falls off the front page, accept it. Don't resubmit for at
  least 72h.
