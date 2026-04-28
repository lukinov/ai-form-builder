# Contributing

Thanks for considering a contribution. The skill is small enough that a single thoughtful PR can move the needle a lot.

## What we're looking for

| Area | Examples |
|---|---|
| **More example schemas** | KYC / onboarding flows, admin panel filters, branching surveys, ecom checkout |
| **Additional UI library adapters** | Chakra UI, Ant Design, shadcn-ui — when the FormEngine adapter exists |
| **MCP server** | Port `scripts/validate_schema.py` to TypeScript, wire `generate_form` tool — see [`mcp-server/README.md`](mcp-server/README.md) |
| **Validator tests** | Property-based tests in `scripts/test_validator.py` |
| **Documentation** | Tutorials, integration guides (Next.js, Remix, RHF transform layer) |
| **Translations** | RU, ES, DE, JA versions of `SKILL.md` |

## Local development

```bash
git clone https://github.com/optimajet/ai-form-builder
cd ai-form-builder

# Run the validator on every example
python skills/ai-form-builder/scripts/validate_schema.py examples/signup/form.json
python skills/ai-form-builder/scripts/validate_schema.py examples/contact/form.json
python skills/ai-form-builder/scripts/validate_schema.py examples/multi-step-onboarding/form.json
python skills/ai-form-builder/scripts/validate_schema.py examples/survey-conditional/form.json
```

CI runs the same checks on every PR.

## Editing the skill prompt

The single source of truth for the skill prompt is
[`skills/ai-form-builder/SKILL.md`](skills/ai-form-builder/SKILL.md).
The Cursor and Windsurf adaptations
([`.cursor/rules/formengine.mdc`](.cursor/rules/formengine.mdc),
[`.windsurf/rules/formengine.md`](.windsurf/rules/formengine.md)) are
shorter mirrors of the same rules — when SKILL.md changes meaningfully,
update them too.

## Adding a new example

1. Create `examples/<your-example>/form.json` and `App.tsx`.
2. Run the validator on `form.json` — it must pass with zero errors.
3. Add a row to `examples/README.md` and the README's example table.
4. Open a PR.

## Adding a new UI library adapter

This requires the corresponding `@react-form-builder/components-<lib>`
package to exist. If it does:

1. Add the type list to `references/component-types.md` and to
   `scripts/validate_schema.py` (the `*_TYPES` set).
2. Add adapter rules to `SKILL.md` (tooltipType, errorType, common
   renames).
3. Add a `react-starter.md` snippet for the App.tsx template.
4. Add at least one example using the new library.

## Code of Conduct

Be kind, be specific, ship what you can, leave it cleaner than you
found it.
