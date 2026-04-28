# Examples

Four reference outputs the skill produces. Each folder has a working `form.json` and a minimal `App.tsx`. Drop into a Vite/Next/CRA project alongside an install of the FormEngine runtime:

```bash
npm install @react-form-builder/core @react-form-builder/components-rsuite rsuite
```

| Example | What it shows |
|---|---|
| [`signup/`](signup/) | Side-by-side name fields, password length validation, required TOS checkbox |
| [`contact/`](contact/) | Multi-line message with `min` length, intro paragraph via `RsStaticContent` |
| [`multi-step-onboarding/`](multi-step-onboarding/) | `RsWizard` + 3 `RsWizardStep`s: account → company → preferences |
| [`survey-conditional/`](survey-conditional/) | `renderWhen` + `validateWhen`: low rating reveals a reason field; "heard elsewhere" reveals a source dropdown |

Open any of these in the [Online FormBuilder](https://formbuilder.formengine.io) to edit visually:

1. Open <https://formbuilder.formengine.io>
2. Click **Import**
3. Paste the contents of `form.json`

You'll get a drag-and-drop editor on top of the same schema.
