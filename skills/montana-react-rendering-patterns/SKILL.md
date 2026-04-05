---
name: montana-react-rendering-patterns
description: React decision-spec skill for consistent conditional rendering, state presentation order, and UI branch structure.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-react","montana-ts","montana-js","montana-frontend-architecture","montana-usecase-delivery"]}}
---

Use this skill when React work involves conditional rendering, view states, component branching, or repeated UI state patterns.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-react`
- `montana-ts`
- `montana-js`
- `montana-frontend-architecture`
- `montana-usecase-delivery`

## Consistency contract (non-negotiables)
- Prefer one stable rendering order for async and data-driven UI states.
- Keep rendering logic readable enough that two agents would choose nearly the same branch structure.
- Do not bury important UI states inside nested ternaries or deeply nested JSX.

## Montana preferred choices
- Prefer rendering order: loading -> error -> empty -> content.
- Prefer early-return branches over nested conditionals inside JSX.
- Prefer small, named booleans when branch conditions are non-trivial.
- Prefer explicit fallback UI over silent `null` returns when the user should understand a missing state.
- Prefer colocating rendering logic with the component that owns the state unless multiple consumers need the abstraction.

## Avoid / anti-patterns
- Nested ternaries for multi-state rendering.
- Mixing loading, error, and content markup in one dense JSX tree.
- Returning `null` for meaningful failure or empty states without explanation.
- Duplicating state solely to make rendering easier.

## Default workflow
1. Identify every user-visible UI state in the component.
2. Put the states in Montana order: loading, error, empty, content.
3. Choose early returns when they make the state machine clearer.
4. Keep JSX focused on the active state rather than embedding every branch inline.
5. Verify accessibility for each rendered branch.

## Decision table
- When a component has asynchronous states, prefer ordered early returns.
- When a branch condition is reused or semantically meaningful, promote it to a named boolean.
- When a component has one trivial optional fragment, inline conditional rendering is acceptable.
- When a component has 3 or more meaningful UI states, avoid nested inline branching and split states clearly.

## Output format
- States identified
- Rendering pattern chosen
- Components affected
- Accessibility or UX notes

## Safety rules
- Ask before broad tree rewrites that change ownership or routing.
- Stop and report when the repo has an established rendering pattern that conflicts with Montana defaults.
- If tests/builds fail, report the smallest actionable failure instead of improvising more structure.
