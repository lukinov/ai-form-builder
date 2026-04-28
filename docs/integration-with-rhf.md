# Integrating with React Hook Form

You don't need React Hook Form (RHF) — FormEngine ships with its own
validation layer. But if your codebase already uses RHF and you want
to keep that as the source of truth, here are the patterns that work.

## Pattern 1 — render FormEngine, lift values via `onFormDataChange`

The simplest path. FormEngine renders the form and you snapshot its
state into your RHF context whenever it changes:

```tsx
import { useForm, FormProvider } from "react-hook-form";
import { FormViewer } from "@react-form-builder/core";
import { view } from "@react-form-builder/components-rsuite";
import formJson from "./form.json";

export default function Page() {
  const methods = useForm();
  const getForm = () => JSON.stringify(formJson);

  return (
    <FormProvider {...methods}>
      <FormViewer
        view={view}
        getForm={getForm}
        onFormDataChange={(data) => {
          // Push every keystroke into RHF state.
          for (const [key, value] of Object.entries(data)) {
            methods.setValue(key, value);
          }
        }}
      />
    </FormProvider>
  );
}
```

Trade-off: RHF's per-field state isn't fully populated (FormEngine
manages its own state). You can still read everything via
`methods.getValues()`.

## Pattern 2 — render hidden inputs into your RHF form

If you absolutely need the form to live inside an RHF `<form>` (e.g.,
your submit handler is the RHF `handleSubmit`), wrap the FormViewer
and synchronise into hidden inputs:

```tsx
import { useEffect } from "react";
import { useFormContext } from "react-hook-form";
import { FormViewer } from "@react-form-builder/core";

function FormEngineBridge({ schema }: { schema: object }) {
  const { register, setValue } = useFormContext();
  return (
    <FormViewer
      view={view}
      getForm={() => JSON.stringify(schema)}
      onFormDataChange={(data) => {
        for (const [k, v] of Object.entries(data)) {
          setValue(k, v, { shouldValidate: true, shouldDirty: true });
        }
      }}
    />
  );
}
```

Combined with `methods.handleSubmit(onValid, onInvalid)`, your existing
RHF submit pipeline keeps working.

## Pattern 3 — drive RHF validations from the schema

If you want RHF as the validator (not FormEngine), translate
`schema.validations` into a Zod resolver at runtime. Sketch:

```ts
import { z } from "zod";
import type { FormSchema } from "./types";

export function buildZod(schema: FormSchema): z.ZodObject<any> {
  const shape: Record<string, z.ZodTypeAny> = {};
  walk(schema.form, (node) => {
    const validations = node.schema?.validations ?? [];
    if (!validations.length || !node.key) return;
    let z_: z.ZodTypeAny = z.string();
    for (const v of validations) {
      switch (v.key) {
        case "required":  z_ = z_.refine((s) => !!s, "Required"); break;
        case "email":     z_ = (z_ as z.ZodString).email(); break;
        case "min":       z_ = (z_ as z.ZodString).min(v.args.limit); break;
        case "max":       z_ = (z_ as z.ZodString).max(v.args.limit); break;
        case "regex":     z_ = (z_ as z.ZodString).regex(new RegExp(v.args.pattern, v.args.flags)); break;
        // ...rest of the FormEngine Zod set
      }
    }
    shape[node.key] = z_;
  });
  return z.object(shape);
}
```

Then plug into RHF:

```tsx
import { zodResolver } from "@hookform/resolvers/zod";
const methods = useForm({ resolver: zodResolver(buildZod(formJson)) });
```

Trade-off: you're maintaining a second validator that has to stay in
sync with FormEngine's. Most teams don't need this — the Pattern 1 lift
is enough.

## When NOT to bridge to RHF

- You're starting a new app — just use FormEngine's validations
  directly. They cover the same ground (Zod-equivalent rule keys), with
  schema-driven config.
- You have one or two forms — the bridge complexity isn't worth the
  consistency.

## See also

- [FormEngine validation reference](https://formengine.io/documentation/formengine-core/validation/)
- [FormEngine event handling](https://formengine.io/documentation/formengine-core/handling-form-data/)
- [React Hook Form docs](https://react-hook-form.com)
