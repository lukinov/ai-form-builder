# React starter — App.tsx templates

The skill always emits one of these `App.tsx` files alongside the schema.
They're minimal on purpose — no companion CSS, no root className, no
`<style>` block. Theming happens at the library provider level.

## RSuite

```tsx
import "rsuite/dist/rsuite.min.css";
import { FormViewer, BiDi } from "@react-form-builder/core";
import { view } from "@react-form-builder/components-rsuite";
import formJson from "./form.json";

const getForm = () => JSON.stringify(formJson);

export default function App() {
  return (
    <div style={{ maxWidth: 720, margin: "40px auto", padding: 16 }}>
      <FormViewer
        view={view}
        getForm={getForm}
        onFormDataChange={(data) => console.log(data)}
        biDi={BiDi.LTR}
      />
    </div>
  );
}
```

```bash
npm install @react-form-builder/core @react-form-builder/components-rsuite rsuite
```

## Material UI

```tsx
import { CssBaseline, ThemeProvider, createTheme } from "@mui/material";
import { FormViewer, BiDi } from "@react-form-builder/core";
import { view } from "@react-form-builder/components-material-ui";
import formJson from "./form.json";

const theme = createTheme();
const getForm = () => JSON.stringify(formJson);

export default function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <div style={{ maxWidth: 720, margin: "40px auto", padding: 16 }}>
        <FormViewer
          view={view}
          getForm={getForm}
          onFormDataChange={(data) => console.log(data)}
          biDi={BiDi.LTR}
        />
      </div>
    </ThemeProvider>
  );
}
```

```bash
npm install @react-form-builder/core @react-form-builder/components-material-ui @mui/material @mui/x-date-pickers @emotion/react @emotion/styled
```

## Mantine

```tsx
import "@mantine/core/styles.css";
import { MantineProvider } from "@mantine/core";
import { FormViewer, BiDi } from "@react-form-builder/core";
import { view } from "@react-form-builder/components-mantine";
import formJson from "./form.json";

const getForm = () => JSON.stringify(formJson);

export default function App() {
  return (
    <MantineProvider>
      <div style={{ maxWidth: 720, margin: "40px auto", padding: 16 }}>
        <FormViewer
          view={view}
          getForm={getForm}
          onFormDataChange={(data) => console.log(data)}
          biDi={BiDi.LTR}
        />
      </div>
    </MantineProvider>
  );
}
```

```bash
npm install @react-form-builder/core @react-form-builder/components-mantine @mantine/core @mantine/hooks @mantine/dates
```

## Reading the submitted data

Two patterns:

**Live updates (recommended for UX feedback):**

```tsx
<FormViewer
  view={view}
  getForm={getForm}
  onFormDataChange={(data) => setLatest(data)}
/>
```

**On-demand (e.g., from a "Submit" button outside the form):**

```tsx
import { useRef } from "react";
import { FormViewer, FormViewerRef } from "@react-form-builder/core";

const viewerRef = useRef<FormViewerRef>(null);

<FormViewer ref={viewerRef} view={view} getForm={getForm} />
<button onClick={() => console.log(viewerRef.current?.formData)}>Submit</button>
```

## Theming — at the library level, not inline

The schema is intentionally free of color/font/border decisions. To
brand the form, configure the library's theme provider in this `App.tsx`:

- **RSuite** — wrap with `<CustomProvider theme={...}>`
- **MUI** — pass a custom `theme` to `<ThemeProvider>`
- **Mantine** — pass `theme` to `<MantineProvider>`

This keeps the JSON portable: it can be edited in the Online FormBuilder,
fed back, served from your CMS, or localized — without touching styling.
