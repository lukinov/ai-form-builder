import "rsuite/dist/rsuite.min.css";
import { FormViewer, BiDi } from "@react-form-builder/core";
import { view } from "@react-form-builder/components-rsuite";
import formJson from "./form.json";

const getForm = () => JSON.stringify(formJson);

export default function App() {
  return (
    <div style={{ maxWidth: 600, margin: "40px auto", padding: 16 }}>
      <FormViewer
        view={view}
        getForm={getForm}
        onFormDataChange={(data) => console.log("contact form data:", data)}
        biDi={BiDi.LTR}
      />
    </div>
  );
}
