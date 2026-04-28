# Signup form example

5-field signup with side-by-side first/last name, email validation, password length validation, and a required Terms-of-Service checkbox.

**Demonstrates:**
- `RsContainer` with `display: flex` for side-by-side fields
- `wrapperCss.any.object.flex: "1"` for equal-width children
- Multiple validation rules per field
- `truthy` validation for consent

**Run it:**

```bash
npm install @react-form-builder/core @react-form-builder/components-rsuite rsuite
# Drop form.json and App.tsx into a Vite/Next/CRA project, then:
npm run dev
```

**Tweak it visually:** open [formbuilder.formengine.io](https://formbuilder.formengine.io) → Import → paste the contents of `form.json`.
