# FormEngine schema anatomy

The exact shape of a FormEngine JSON form. Read this before generating
any schema. The validator (`scripts/validate_schema.py`) enforces every
rule on this page.

## Top level

```json
{
  "version": 1,
  "form": { "type": "Screen", "key": "root", "children": [ ... ] },
  "tooltipType": "RsTooltip",
  "errorType": "RsErrorMessage",
  "localization": {}
}
```

| Field | Required | Notes |
|---|---|---|
| `form` | yes | The component tree. **Root must be `type: "Screen"`** — never `Form`. |
| `tooltipType` | recommended | `RsTooltip` / `MuiTooltip` / `MtTooltip` depending on library |
| `errorType` | recommended | `RsErrorMessage` / `MuiErrorWrapper` / `MtErrorWrapper` |
| `version` | optional | integer |
| `localization` | optional | object keyed by locale → keyed by string-id |

## Component node

```json
{
  "type": "RsInput",
  "key": "email",
  "props": {
    "label":       { "value": "Email" },
    "placeholder": { "value": "you@example.com" },
    "type":        { "value": "email" }
  },
  "schema": {
    "validations": [
      { "key": "required" },
      { "key": "email" }
    ]
  },
  "css": { "any": { "object": { "marginBottom": "12px" } } },
  "wrapperCss": { "any": { "object": { "flex": "1" } } },
  "renderWhen": { "jsCode": "data.subscribe === true" }
}
```

| Field | Notes |
|---|---|
| `type` | Must exist in the chosen library — see `component-types.md` |
| `key` | **Unique within the tree.** Used as the data field name in the result |
| `props` | Object of `{ propName: wrappedValue }`. **Every value is wrapped** |
| `schema.validations` | Array of `{ key, args? }` entries — see Validations |
| `children` | Array of nested component nodes (containers only) |
| `css` | Layout-only styling on the component itself |
| `wrapperCss` | Layout-only styling on the component's wrapper |
| `renderWhen` | Show/hide expression — `{ "jsCode": "..." }` |
| `validateWhen` | Conditional validation — same shape as `renderWhen` |

### Wrapped values

Every value inside `props` is one of:

```json
{ "value":   "literal text" }
{ "value":   42 }
{ "value":   true }
{ "value":   ["a", "b"] }
{ "jsCode":  "data.firstName + ' ' + data.lastName" }
{ "action":  "openModal" }
```

**Bare strings or numbers are forbidden.** This is the single most common
foot-gun:

```json
"label": "Email"               ❌
"label": { "value": "Email" }  ✅
```

## Validations

Validation rules live under `schema.validations` on the component that
*owns the data* — NEVER on the Screen root. The valid keys are the
FormEngine Zod set:

| Key | `args` shape | Example |
|---|---|---|
| `required` | none | `{ "key": "required" }` |
| `nonEmpty` | none | for arrays/strings |
| `min` | `{ "limit": N }` | strings: min length; numbers: min value |
| `max` | `{ "limit": N }` | |
| `length` | `{ "limit": N }` | exact length |
| `email` | none | |
| `url` | none | |
| `uuid` | none | |
| `ip` | none | |
| `datetime` | none | ISO-8601 |
| `regex` | `{ "pattern": "...", "flags": "i" }` | |
| `includes` | `{ "value": "..." }` | substring |
| `startsWith` | `{ "value": "..." }` | |
| `endsWith` | `{ "value": "..." }` | |
| `lessThan` | `{ "value": N }` | exclusive |
| `moreThan` | `{ "value": N }` | exclusive |
| `integer` | none | |
| `multipleOf` | `{ "value": N }` | |
| `truthy` | none | for booleans / consent checkboxes |
| `falsy` | none | |

> **There is no `minLength` / `maxLength`.** Use `min` / `max` with
> `args.limit`.

Add a custom message:

```json
{ "key": "min", "args": { "limit": 8 }, "message": "Password must be at least 8 characters" }
```

## Layout — `css` and `wrapperCss`

Both fields take this shape:

```json
"css": { "any": { "object": { "<layout-key>": "<value>", ... } } }
```

The `any` / `object` wrapper exists because FormEngine supports
breakpoint-keyed objects in the same slot — `any` means "all
breakpoints". Don't try to flatten it.

**Layout keys allowed:**
`display`, `position`, `top/right/bottom/left/inset`, `zIndex`, `order`,
`overflow*`, `boxSizing`, `width/height/min*/max*`,
`margin*`, `padding*`, `gap`, `rowGap`, `columnGap`,
`flex*`, `align*`, `justify*`, `place*`, `grid*`, `aspectRatio`.

**Visual keys forbidden** (move to library theme provider):
`color`, `background*`, `border*`, `boxShadow`, `borderRadius`,
`font*`, `text*`, `letterSpacing`, `lineHeight`, `opacity`,
`transform`, `filter`, `outline*`, `cursor`, `transition*`,
`animation*`, `pointerEvents`, `userSelect`.

The legacy field name `style` is **not supported** — never emit it.

## Side-by-side fields (the canonical pattern)

```json
{
  "type": "RsContainer",
  "key": "name-row",
  "css": { "any": { "object": { "display": "flex", "gap": "16px" } } },
  "children": [
    { "type": "RsInput", "key": "firstName",
      "props": { "label": { "value": "First name" } },
      "wrapperCss": { "any": { "object": { "flex": "1" } } } },
    { "type": "RsInput", "key": "lastName",
      "props": { "label": { "value": "Last name" } },
      "wrapperCss": { "any": { "object": { "flex": "1" } } } }
  ]
}
```

That's it. No grid, no Stack, no separate flexbox component — `RsContainer`
with `display: flex` IS the mechanism.

## Section heading + group

Don't smuggle `<h2>` into `RsStaticContent`. Use `RsCard` with `header`:

```json
{
  "type": "RsCard",
  "key": "billing-section",
  "props": { "header": { "value": "Billing address" } },
  "children": [ ... ]
}
```

For a sub-section inside a card, nest another `RsCard`.

## Conditional rendering

```json
{
  "type": "RsInput",
  "key": "phone",
  "props": { "label": { "value": "Phone" } },
  "renderWhen":   { "jsCode": "data.email && data.email.length > 0" },
  "validateWhen": { "jsCode": "data.email && data.email.length > 0" }
}
```

`data` is the form's current values. Use `renderWhen` to hide the
component, and `validateWhen` if you only want validations to fire when
visible.
