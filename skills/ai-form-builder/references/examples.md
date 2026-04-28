# Reference examples

Four complete schemas — read them when you need to calibrate style and
completeness on a new form. All use RSuite by default; the patterns
translate directly to MUI / Mantine.

> Full runnable code for each example lives in the repo's `examples/`
> folder. This file is the at-a-glance reference.

## 1. Signup form (5 fields, validation, password)

Field set: full name, email, password, confirm password, T&Cs checkbox.
Notes: side-by-side first/last name, password validation,
truthy validation on consent.

```json
{
  "version": 1,
  "tooltipType": "RsTooltip",
  "errorType": "RsErrorMessage",
  "form": {
    "type": "Screen",
    "key": "signup",
    "children": [
      {
        "type": "RsCard",
        "key": "card",
        "props": { "header": { "value": "Create your account" } },
        "children": [
          {
            "type": "RsContainer",
            "key": "name-row",
            "css": { "any": { "object": { "display": "flex", "gap": "16px" } } },
            "children": [
              {
                "type": "RsInput", "key": "firstName",
                "props": { "label": { "value": "First name" } },
                "wrapperCss": { "any": { "object": { "flex": "1" } } },
                "schema": { "validations": [{ "key": "required" }] }
              },
              {
                "type": "RsInput", "key": "lastName",
                "props": { "label": { "value": "Last name" } },
                "wrapperCss": { "any": { "object": { "flex": "1" } } },
                "schema": { "validations": [{ "key": "required" }] }
              }
            ]
          },
          {
            "type": "RsInput", "key": "email",
            "props": { "label": { "value": "Email" }, "type": { "value": "email" } },
            "schema": { "validations": [{ "key": "required" }, { "key": "email" }] }
          },
          {
            "type": "RsInput", "key": "password",
            "props": { "label": { "value": "Password" }, "type": { "value": "password" } },
            "schema": {
              "validations": [
                { "key": "required" },
                { "key": "min", "args": { "limit": 8 }, "message": "At least 8 characters" }
              ]
            }
          },
          {
            "type": "RsCheckbox", "key": "tos",
            "props": { "label": { "value": "I agree to the Terms of Service" } },
            "schema": { "validations": [{ "key": "truthy", "message": "You must agree to continue" }] }
          },
          {
            "type": "RsButton", "key": "submit",
            "props": { "appearance": { "value": "primary" }, "block": { "value": true } }
          }
        ]
      }
    ]
  }
}
```

## 2. Contact form (4 fields, multiline message)

Field set: name, email, subject, message. Trivial validation.

```json
{
  "version": 1,
  "tooltipType": "RsTooltip",
  "errorType": "RsErrorMessage",
  "form": {
    "type": "Screen",
    "key": "contact",
    "children": [
      {
        "type": "RsCard",
        "key": "card",
        "props": { "header": { "value": "Get in touch" } },
        "children": [
          {
            "type": "RsInput", "key": "name",
            "props": { "label": { "value": "Your name" } },
            "schema": { "validations": [{ "key": "required" }] }
          },
          {
            "type": "RsInput", "key": "email",
            "props": { "label": { "value": "Email" }, "type": { "value": "email" } },
            "schema": { "validations": [{ "key": "required" }, { "key": "email" }] }
          },
          {
            "type": "RsInput", "key": "subject",
            "props": { "label": { "value": "Subject" } },
            "schema": { "validations": [{ "key": "required" }] }
          },
          {
            "type": "RsTextArea", "key": "message",
            "props": { "label": { "value": "Message" }, "rows": { "value": 5 } },
            "schema": {
              "validations": [
                { "key": "required" },
                { "key": "min", "args": { "limit": 20 }, "message": "Tell us a bit more (20+ chars)" }
              ]
            }
          },
          {
            "type": "RsButton", "key": "send",
            "props": { "appearance": { "value": "primary" } }
          }
        ]
      }
    ]
  }
}
```

## 3. Multi-step onboarding (RsWizard)

Three steps: account → company → preferences. Use `RsWizard` +
`RsWizardStep` — never roll your own step UI.

```json
{
  "form": {
    "type": "Screen",
    "key": "onboarding",
    "children": [
      {
        "type": "RsWizard",
        "key": "wiz",
        "children": [
          {
            "type": "RsWizardStep",
            "key": "step-account",
            "props": { "title": { "value": "Account" } },
            "children": [ /* RsInput email, RsInput password */ ]
          },
          {
            "type": "RsWizardStep",
            "key": "step-company",
            "props": { "title": { "value": "Company" } },
            "children": [ /* RsInput companyName, RsDropdown industry */ ]
          },
          {
            "type": "RsWizardStep",
            "key": "step-prefs",
            "props": { "title": { "value": "Preferences" } },
            "children": [ /* RsCheckboxGroup channels, RsToggle marketing */ ]
          }
        ]
      }
    ]
  }
}
```

## 4. Survey with conditional fields (`renderWhen`)

"Did you hear about us elsewhere?" → if yes, show a dropdown of
sources. Conditional rendering tied to a checkbox.

```json
{
  "form": {
    "type": "Screen",
    "key": "survey",
    "children": [
      {
        "type": "RsRate", "key": "satisfaction",
        "props": { "label": { "value": "How satisfied are you?" }, "max": { "value": 5 } },
        "schema": { "validations": [{ "key": "required" }] }
      },
      {
        "type": "RsCheckbox", "key": "heardElsewhere",
        "props": { "label": { "value": "I first heard about you from another source" } }
      },
      {
        "type": "RsDropdown", "key": "source",
        "props": {
          "label": { "value": "Where did you hear about us?" },
          "data": { "value": [
            { "label": "Twitter", "value": "twitter" },
            { "label": "Hacker News", "value": "hn" },
            { "label": "A friend", "value": "friend" },
            { "label": "Other", "value": "other" }
          ] }
        },
        "renderWhen":   { "jsCode": "data.heardElsewhere === true" },
        "validateWhen": { "jsCode": "data.heardElsewhere === true" },
        "schema": { "validations": [{ "key": "required" }] }
      },
      {
        "type": "RsTextArea", "key": "comments",
        "props": { "label": { "value": "Anything else? (optional)" }, "rows": { "value": 3 } }
      }
    ]
  }
}
```
