---
name: montana-pattern-conditional-rendering
description: Pattern skill for Montana conditional rendering: order states clearly, prefer early returns, and keep branch structure readable and accessible.
metadata: {"montana":{"category":"pattern","composesWith":["montana-global-contract","montana-react","montana-react-rendering-patterns","montana-react-state-ownership","montana-ts","montana-js","montana-frontend-architecture","montana-usecase-delivery"]}}
---

Use this skill when UI work involves multiple visible states and you want a repeatable Montana rendering shape.

## Category
- Pattern

## Works with
- `montana-global-contract`
- `montana-react`
- `montana-react-rendering-patterns`
- `montana-react-state-ownership`
- `montana-ts`
- `montana-js`
- `montana-frontend-architecture`
- `montana-usecase-delivery`

## Preferred pattern
1. Identify all user-visible states.
2. Order them as loading -> error -> empty -> content unless the repo intentionally differs.
3. Prefer early-return branches for meaningful state transitions.
4. Keep each branch focused on one state and its accessible UI.
5. Use named booleans when branch conditions become non-trivial.

## Anti-patterns
- Nested ternaries for multi-state UI.
- Mixing all states into one dense JSX tree.
- Returning `null` when the user should receive meaningful state feedback.
- Duplicating state just to make rendering logic easier.

## Rationale
- Early-return state ordering reduces variance between agents.
- Clear branches make it easier to test and review UI state behavior.
- Explicit state handling leads to more consistent accessibility outcomes.

## Decision table
- When there are 3 or more meaningful states, prefer ordered early returns.
- When a single optional fragment is trivial, inline conditional rendering is acceptable.
- When a branch condition is reused or semantically important, promote it to a named boolean.
- When empty or error states are meaningful to the user, render them explicitly.

## Default workflow
1. Identify every user-visible state in the component.
2. Put the states in Montana order: loading, error, empty, content.
3. Choose early returns when they make the state machine clearer.
4. Promote reused or non-trivial branch conditions into named booleans.
5. Verify accessibility and readability of each rendered branch.

## Output format
- States identified
- Rendering pattern applied
- Components affected
- Accessibility notes

## Safety rules
- Ask before restructuring large component trees just to normalize rendering style.
- If the repo already has a stronger rendering convention, follow it and report the Montana difference if relevant.
