---
name: montana-react-state-ownership
description: React decision-spec skill for consistent Montana choices around local state, derived state, lifting state, and hook extraction.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-react","montana-react-rendering-patterns","montana-ts","montana-js","montana-frontend-architecture","montana-usecase-delivery"]}}
---

Use this skill when React work involves deciding where state should live, whether state should be derived, or whether a hook/component extraction is justified.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-react`
- `montana-react-rendering-patterns`
- `montana-ts`
- `montana-js`
- `montana-frontend-architecture`
- `montana-usecase-delivery`

## Consistency contract (non-negotiables)
- Keep state as close as practical to the component that owns it.
- Prefer derived state over duplicated state whenever the value can be computed reliably.
- Extract hooks or lift state only when ownership genuinely spans multiple consumers or boundaries.

## Montana preferred choices
- Prefer local component state by default.
- Prefer lifting state only when two or more siblings, persistence/navigation, or a shared feature boundary actually require it.
- Prefer deriving booleans, labels, and filtered collections from source state instead of storing copies.
- Prefer extracting a hook when stateful logic is reused, has side-effect orchestration, or obscures the component.
- Prefer keeping one-off logic in the component when extraction would add indirection without reuse or clarity gains.

## Avoid / anti-patterns
- Duplicating server data in multiple local state variables just to simplify rendering.
- Extracting hooks for one-time logic that is easier to read inline.
- Lifting state to parent modules "just in case."
- Storing values that can be directly derived from props or existing state.

## Decision table
- When only one component owns and uses the state, keep it local.
- When multiple siblings need coordinated updates, lift to the nearest shared owner.
- When a value can be recomputed cheaply from current inputs, derive it instead of storing it.
- When stateful logic is reused or mixes effects and event coordination, extract a hook.
- When extraction hides ownership or adds unclear indirection, keep the logic in the component.

## Default workflow
1. Identify who reads the state and who mutates it.
2. Decide whether the value is source state or derived state.
3. Keep the state in the narrowest owner that satisfies the data flow.
4. Extract a hook only when reuse or clarity clearly improves.
5. Verify that the change did not duplicate sources of truth.

## Output format
- State ownership decision
- Components/hooks affected
- Why the chosen owner is correct
- Commands run

## Safety rules
- Ask before introducing a new state library or cross-feature state abstraction.
- Ask before lifting state across major feature boundaries.
- Stop and report when the repo has an established ownership pattern that conflicts with Montana defaults.
