---
name: montana-react-form-patterns
description: React decision-spec skill for Montana form handling, submit flow, validation feedback, disabled states, and error presentation.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-react","montana-react-rendering-patterns","montana-react-state-ownership","montana-ts","montana-js","montana-ts-runtime-validation","montana-frontend-architecture","montana-usecase-delivery","montana-pattern-regression-bugfix"]}}
---

Use this skill when React work involves forms, validation feedback, submit states, or choosing between multiple clean form implementations.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-react`
- `montana-react-rendering-patterns`
- `montana-react-state-ownership`
- `montana-ts`
- `montana-js`
- `montana-ts-runtime-validation`
- `montana-frontend-architecture`
- `montana-usecase-delivery`
- `montana-pattern-regression-bugfix`

## Consistency contract (non-negotiables)
- Forms should expose a stable Montana submit flow: input, validate, submit, success/failure feedback.
- Disabled, loading, and error states should be explicit and visible to users.
- Validation and error presentation should be accessible and predictable.

## Montana preferred choices
- Prefer controlled inputs by default unless the repo or use case clearly benefits from uncontrolled form handling.
- Prefer explicit submit state such as `isSubmitting` or equivalent when the request is asynchronous.
- Prefer disabling the submit button during in-flight submission when duplicate requests would be problematic.
- Prefer labels, described-by relationships, and accessible error messaging.
- Prefer boundary validation near the submit adapter or form state entry point.

## Avoid / anti-patterns
- Hidden submit failures with no user-visible feedback.
- Multiple competing sources of truth for the same form value.
- Nested conditional form rendering that obscures submit, error, and success states.
- Disabling inputs or submit buttons with no visible reason when a loading/error state exists.

## Decision table
- When a form submission is async, track explicit submit state and reflect it in UI controls.
- When validation errors are user-facing, render them accessibly and near the relevant control or summary surface.
- When the form is simple and app-owned, controlled inputs are the Montana default.
- When input normalization or external payload shaping is needed, perform it at the submit/boundary layer.

## Default workflow
1. Identify the form owner and submit boundary.
2. Decide the state model: values, validation, submit state, and feedback state.
3. Keep the form controlled unless there is a clear reason not to.
4. Make loading, error, and disabled states explicit.
5. Verify accessibility and submit behavior.

## Output format
- Form pattern chosen
- Components/hooks affected
- Commands run
- Accessibility or UX notes

## Safety rules
- Ask before introducing a new form library or broad form architecture change.
- Stop and report if the repo has a stable form pattern that should take precedence over Montana defaults.
- If tests/builds fail, report the narrowest actionable failure instead of improvising unrelated changes.
