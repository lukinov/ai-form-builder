# Changelog

All notable changes to this project will be documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.1.0] — 2026-04-28

### Added
- Initial release of the FormEngine AI Form Builder skill.
- `skills/ai-form-builder/SKILL.md` — full skill prompt with hard
  rules around layout-only `css`, no-HTML-in-strings, and the FormEngine
  Zod validation set.
- `references/` — schema anatomy, component-types tables (RSuite / MUI /
  Mantine), reference examples, React starter templates.
- `scripts/validate_schema.py` — Python validator that catches the 30+
  common failure modes (unknown component types, unwrapped prop values,
  visual styling in `css`, smuggled HTML, invalid validation rule keys).
- `.claude-plugin/` — Claude Code plugin manifest.
- `.cursor/rules/formengine.mdc` — Cursor rule.
- `.windsurf/rules/formengine.md` — Windsurf rule.
- `mcp-server/` — scaffold + roadmap.
- `examples/` — four runnable reference forms (signup, contact,
  multi-step onboarding, conditional survey).

[Unreleased]: https://github.com/optimajet/ai-form-builder/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/optimajet/ai-form-builder/releases/tag/v0.1.0
