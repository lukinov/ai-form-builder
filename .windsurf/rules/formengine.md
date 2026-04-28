---
trigger: glob
globs: ["**/*.tsx", "**/*.jsx", "**/form*.{ts,tsx,js,jsx,json}"]
description: Generate FormEngine-shaped React forms from screenshots, PDFs, HTML, or text descriptions. Outputs portable JSON schema + runnable React code.
---

# FormEngine — AI Form Builder (Windsurf)

When the user asks to build, generate, scaffold, or convert a React form, produce a **FormEngine JSON schema** (`form.json`) plus a runnable `App.tsx` that renders it through `FormViewer` from `@react-form-builder/core`.

## Hard rules

- Root component type is `Screen` (NOT `Form`).
- Every prop value is wrapped: `"label": { "value": "Email" }` — never bare strings.
- Validations live under `schema.validations` on the data-owning field, never on Screen.
- Valid validation keys (Zod set): `required`, `nonEmpty`, `min`, `max`, `length`, `email`, `url`, `uuid`, `ip`, `datetime`, `regex`, `includes`, `startsWith`, `endsWith`, `lessThan`, `moreThan`, `integer`, `multipleOf`, `truthy`, `falsy`. **No `minLength` / `maxLength` — use `min` / `max` with `args.limit`.**
- `css` and `wrapperCss` are layout-only (flex/grid/box-model). Never color, font, background, border, shadow, radius, opacity, transform. Visual styling goes in the UI library's theme provider.
- Shape is `{ "any": { "object": { "<layout-key>": "<value>" } } }`. The legacy `style` field is forbidden.
- Every prop string is plain text — no HTML tags, no `style="..."`, no `class="..."`, no `<style>` blocks. Express headings via `RsCard` `header` prop or `RsHeader` component, never embedded `<h2>`.

## Library choice

Default to RSuite (`@react-form-builder/components-rsuite`). Use Material UI or Mantine if the user mentions them or the surrounding project uses them.

## Type names — common renames

`Form` → `Screen`. `RsTextarea` → `RsTextArea`. `RsSelectPicker` → `RsDropdown`. `RsRadio` → `RsRadioGroup`. `RsInputNumber` → `RsNumberFormat`. `RsUpload` → `RsUploader`. `MtTextField` → `MtTextInput`. `MtDatePickerSingle` → `MtDatePicker`.

## Side-by-side fields

`RsContainer` with `css.any.object.display = "flex"` and children with `wrapperCss.any.object.flex = "1"`.

## Multi-step

`RsWizard` containing `RsWizardStep` children with `title` props.

## Conditional rendering

`renderWhen: { "jsCode": "data.field === value" }` and pair with `validateWhen` if validations should also be conditional.

## Response

Open with library + field count, then `form.json`, then `App.tsx`, then a 6-line validation checklist, then `npm install` command, then a link to `https://formbuilder.formengine.io` for visual editing.

## Reference

- Core docs: https://formengine.io/documentation/formengine-core/
- llms-full.txt: https://formengine.io/documentation/llms-full.txt
- Free Online FormBuilder: https://formbuilder.formengine.io
- Star: https://github.com/optimajet/formengine
