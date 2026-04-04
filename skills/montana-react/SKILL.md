---
name: montana-react
description: React frontend skill for component design, state flow, accessibility, and maintainable UI implementation.
metadata: {"montana":{"category":"framework","composesWith":["montana-ts","montana-js","montana-frontend-architecture","montana-usecase-delivery"]}}
---

Use this skill when building or updating React-based frontend applications.

## Category
- Framework

## Works with
- `montana-ts`
- `montana-js`
- `montana-frontend-architecture`
- `montana-usecase-delivery`

## Consistency contract (non-negotiables)
- Prefer existing project patterns over personal preference.
- Keep components focused, composable, and accessible.
- Avoid unnecessary abstractions, memoization, or state duplication.
- Verify behavior through the repo’s test/build/lint flow when available.

## Montana defaults
Apply these when the repo does not already specify otherwise:
- Prefer function components.
- Keep state close to where it is used.
- Derive state instead of duplicating it when practical.
- Add JSDoc only for exported components/hooks whose behavior is not obvious.
- Favor clear props and explicit event handling.
- Respect accessibility basics: labels, button semantics, keyboard flow, disabled states.

## Default workflow
1. Identify the UI entrypoint and component ownership.
2. Understand data flow, state ownership, and side effects before editing.
3. Make the smallest UI change that satisfies the request.
4. Verify rendering, interaction states, and accessibility expectations.
5. Run repo checks and report outcomes.

## Output format
- What changed
- Components/hooks affected
- Commands run
- Accessibility or UX notes

## Safety rules
- Ask before introducing a new state library or routing pattern.
- Ask before large component tree rewrites.
- If build/tests/lint fail, stop and report the smallest actionable failure.

## Templates
- Use `{baseDir}/templates/component-template.md`
- Use `{baseDir}/templates/hook-template.md`
- Use `{baseDir}/templates/accessibility-checklist.md`
