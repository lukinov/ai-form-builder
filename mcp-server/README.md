# FormEngine MCP server (roadmap)

> **Status:** scaffolded, not yet shipped. Looking for contributors —
> see the [`help wanted`](https://github.com/optimajet/ai-form-builder/labels/help%20wanted)
> issues.

A standalone Model Context Protocol server that exposes the same
form-generation logic as the Claude skill / Cursor rule, but as MCP
tools any IDE or API can call.

## Why an MCP server

The skill / Cursor rule are great for one-off form generation in chat.
But:

- VS Code, Zed, and other IDEs don't load skills — they need MCP.
- CI / CD pipelines that auto-generate forms from a Figma export need
  programmatic access.
- Anthropic's API users want to call this without inlining the full
  SKILL.md as a system prompt.

An MCP server packages the validation script, type tables, and prompt
strategy into three deterministic tools.

## Planned tools

| Tool | Input | Output |
|---|---|---|
| `generate_form` | `{ description, library?, target?: { framework: "react" / "next" } }` | `{ schema: <form.json>, app_tsx: <string>, report: <validation-result> }` |
| `validate_schema` | `{ schema, library? }` | `{ ok: bool, errors: [...], warnings: [...] }` |
| `list_components` | `{ library: "rsuite" / "mui" / "mantine" }` | `{ types: [...] }` — all valid component types for the chosen library |

Optional:

| Tool | |
|---|---|
| `import_html_form` | parse an HTML form string into a FormEngine schema |
| `to_online_builder_link` | encode a schema and return a `formbuilder.formengine.io?import=` URL |

## Implementation plan

```
mcp-server/
├── src/
│   ├── index.ts             # MCP entrypoint
│   ├── tools/
│   │   ├── generate_form.ts
│   │   ├── validate_schema.ts
│   │   └── list_components.ts
│   ├── validator/           # port of scripts/validate_schema.py
│   └── types/               # canonical component type tables (shared)
├── package.json
├── tsconfig.json
└── README.md
```

Built on the [official Anthropic MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk).

## Distribution targets

When shipped:

- npm: `@formengine/mcp-server`
- PR to <https://github.com/punkpeye/awesome-mcp-servers>
- Anthropic Claude Desktop config example
- VS Code extension `claude-mcp` config example

## Help wanted

Pre-shipping work that would unblock this:

1. Port `scripts/validate_schema.py` → TypeScript (the validator
   logic is pure functional)
2. Wire the SKILL.md prompt into `generate_form` (which then calls a
   downstream LLM — Claude / OpenAI / local — to produce schemas)
3. Write Vitest tests around the 4 reference example schemas in
   `examples/`

If interested, comment on the relevant `help wanted` issue or open a
draft PR.
