# LinkedIn launch post

> LinkedIn audience leans senior / engineering manager / decision-maker.
> Tone: less playful, more "useful tool I built". Length: 1300–1500
> chars (LinkedIn engagement peak).

---

We've been shipping forms in React apps for years. The same pattern keeps showing up:

→ A designer hands over a Figma frame  
→ An engineer translates it to JSX  
→ Validations get bolted on inconsistently  
→ Every text change is a code change  
→ Localization is an afterthought  
→ The designer can never open the form again

This weekend we open-sourced something that fixes a chunk of this:

**ai-form-builder** — drop a screenshot, PDF, or text description of a form into Claude Code, Cursor, or Windsurf, and get back a production-ready React form with a validated JSON schema.

Three things make it different from "just ask an LLM":

1. **Schema, not JSX.** The output is portable JSON that round-trips through a free visual editor — the designer can drag fields again.

2. **Real validator.** A Python script catches the 30+ failure modes LLMs hit (wrong component types, smuggled HTML, broken validation rule keys). CI runs it on every PR.

3. **Three install shapes.** Claude Skill, Cursor Rule, Windsurf Rule. MCP server on the roadmap.

It's MIT, built on top of FormEngine Core (also MIT). No SaaS, no per-submission fees, no vendor lock.

Repo: github.com/optimajet/ai-form-builder

If you've been writing forms by hand — try it. If you've been using a no-code SaaS for forms but wished you owned the React code — try it.

I'd love to know what forms are slowest in your codebase. The next 4 examples I add are coming from comments here.

#React #AI #DeveloperTools #OpenSource #FormEngine

---

## Posting notes

- **Best time:** Tuesday or Wednesday, 8–10am PT (LinkedIn engagement peak for B2B/dev).
- **First comment:** drop the GIF + a "I'll generate a schema for any form screenshot you reply with" offer. Drives replies.
- **Tag:** if there are former colleagues at React / Vercel / Anthropic, tag them in a follow-up comment, not in the post.
- **Don't link in the post body** — LinkedIn algorithmically suppresses posts with external links. Drop the GitHub link in the first comment.
