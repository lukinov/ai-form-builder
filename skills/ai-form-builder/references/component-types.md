# Component types — source of truth

The validator uses the same lists. If a type isn't here, don't emit it.
For the most current list, check the package source:
- RSuite: <https://www.npmjs.com/package/@react-form-builder/components-rsuite>
- MUI:    <https://www.npmjs.com/package/@react-form-builder/components-material-ui>
- Mantine:<https://www.npmjs.com/package/@react-form-builder/components-mantine>

## RSuite (`@react-form-builder/components-rsuite`)

### Containers / structure

| Type | Use for |
|---|---|
| `Screen` | Root only |
| `RsContainer` | Generic flex/grid container — side-by-side fields |
| `RsCard` | Section with optional `header` prop |
| `RsHeader` | Standalone heading text |
| `RsDivider` | Visible separator |
| `RsStaticContent` | Plain-text help copy (no markup) |
| `RsWizard` | Multi-step form |
| `RsWizardStep` | Single step inside `RsWizard` |

### Inputs

| Type | HTML equivalent | Notes |
|---|---|---|
| `RsInput` | `<input type=text/email/password>` | Set via `type` prop |
| `RsTextArea` | `<textarea>` | **Capital A** |
| `RsNumberFormat` | `<input type=number>` | Locale-aware |
| `RsDatePicker` | `<input type=date>` | |
| `RsDateRangePicker` | range version | |
| `RsTimePicker` | time only | |
| `RsCheckbox` | single | |
| `RsCheckboxGroup` | multi | |
| `RsRadioGroup` | radios | NOT `RsRadio` |
| `RsToggle` | yes/no switch | |
| `RsDropdown` | `<select>` | NOT `RsSelectPicker` |
| `RsTagPicker` | multi-select tags | |
| `RsCheckPicker` | multi-select with search | |
| `RsCascader` | hierarchical dropdown | |
| `RsAutoComplete` | typeahead | |
| `RsInputMask` | masked input | |
| `RsColorPicker` | color | |
| `RsRate` | star rating | |
| `RsSlider` | single | |
| `RsRangeSlider` | range | |
| `RsUploader` | `<input type=file>` | NOT `RsUpload` |
| `RsButton` | submit / action | |

### Common props

`label`, `placeholder`, `helperText`, `disabled`, `readOnly`, `defaultValue`,
`type` (for `RsInput` — `text` / `email` / `password`),
`data` (for select-likes — array of `{ label, value }`),
`block` (full width),
`size` (`sm` / `md` / `lg`).

## Material UI (`@react-form-builder/components-material-ui`)

### Containers

| Type | Use for |
|---|---|
| `Screen` | Root |
| `MuiBox` | Generic container |
| `MuiCard` | Section card |
| `MuiTypography` | Heading / paragraph |
| `MuiDivider` | Separator |
| `MuiStaticContent` | Plain-text content |
| `MuiStepper` / `MuiStep` | Multi-step |

### Inputs

| Type | Notes |
|---|---|
| `MuiTextField` | All text-like inputs (text/email/password/number) — `type` prop |
| `MuiSelect` | dropdown |
| `MuiAutocomplete` | typeahead / multi |
| `MuiCheckbox` | single |
| `MuiRadioGroup` | radios |
| `MuiSwitch` | yes/no |
| `MuiSlider` | |
| `MuiRating` | stars |
| `MuiDatePicker` | NOT `MuiDatePickerSingle` |
| `MuiTimePicker` | |
| `MuiDateTimePicker` | |
| `MuiButton` | |
| `MuiIconButton` | |

`tooltipType: "MuiTooltip"`, `errorType: "MuiErrorWrapper"`.

## Mantine (`@react-form-builder/components-mantine`)

### Containers

| Type | Use for |
|---|---|
| `Screen` | Root |
| `MtContainer` | Generic |
| `MtCard` | Section |
| `MtTitle` | Heading |
| `MtText` | Paragraph |
| `MtDivider` | Separator |
| `MtStaticContent` | Plain text |
| `MtStepper` / `MtStepperStep` | Multi-step |

### Inputs

| Type | Notes |
|---|---|
| `MtTextInput` | text — NOT `MtTextField` |
| `MtTextarea` | NOT `MtTextArea` (lowercase a) |
| `MtPasswordInput` | dedicated |
| `MtNumberInput` | numeric |
| `MtJsonInput` | JSON editor |
| `MtSelect` | dropdown |
| `MtMultiSelect` | multi |
| `MtAutocomplete` | typeahead |
| `MtCheckbox` / `MtCheckboxGroup` | |
| `MtRadioGroup` | |
| `MtSwitch` | |
| `MtSlider` / `MtRangeSlider` | |
| `MtRating` | |
| `MtDatePicker` / `MtDateTimePicker` / `MtMonthPicker` / `MtYearPicker` | rich set |
| `MtTimeInput` | |
| `MtColorPicker` / `MtColorInput` | Mantine-only |
| `MtFileInput` | |
| `MtSegmentedControl` | tabs-as-input |
| `MtButton` | |

`tooltipType: "MtTooltip"`, `errorType: "MtErrorWrapper"`.

## Common renames — wrong → right

| Wrong | Right | Why |
|---|---|---|
| `Form` | `Screen` | Root type |
| `RsForm` | `RsCard` or `RsContainer` | Doesn't exist |
| `RsSelectPicker` | `RsDropdown` | Renamed in FormEngine |
| `RsRadio` | `RsRadioGroup` | No standalone radio |
| `RsTextarea` | `RsTextArea` | Capital A |
| `RsInputNumber` | `RsNumberFormat` | |
| `RsUpload` | `RsUploader` | |
| `MtDatePickerSingle` | `MtDatePicker` | |
| `MtTextField` | `MtTextInput` | MUI name leaked |
| `MtTextArea` | `MtTextarea` | Lowercase a |
