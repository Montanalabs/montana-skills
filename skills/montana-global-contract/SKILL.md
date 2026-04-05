---
name: montana-global-contract
description: Montana-wide operating contract for predictable agent behavior, minimal diffs, verification, and consistent reporting.
metadata: {"montana":{"category":"global","composesWith":["montana-intake","montana-rust","montana-go","montana-py","montana-ts","montana-js","montana-react","montana-frontend-architecture","montana-backend-architecture","montana-usecase-delivery","montana-release","montana-ts-style-decisions","montana-ts-runtime-validation","montana-ts-error-patterns","montana-react-rendering-patterns","montana-react-state-ownership","montana-react-form-patterns","montana-go-service-patterns","montana-go-http-boundaries","montana-go-testing-patterns","montana-rust-error-patterns","montana-rust-module-boundaries","montana-rust-testing-patterns","montana-pattern-regression-bugfix","montana-pattern-conditional-rendering"]}}
---

Use this skill as the Montana baseline whenever predictable outcomes matter more than agent preference.

## Category
- Global

## Works with
- `montana-intake`
- `montana-rust`
- `montana-go`
- `montana-py`
- `montana-ts`
- `montana-js`
- `montana-react`
- `montana-frontend-architecture`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-release`
- `montana-ts-style-decisions`
- `montana-ts-runtime-validation`
- `montana-ts-error-patterns`
- `montana-react-rendering-patterns`
- `montana-react-state-ownership`
- `montana-react-form-patterns`
- `montana-go-service-patterns`
- `montana-go-http-boundaries`
- `montana-go-testing-patterns`
- `montana-rust-error-patterns`
- `montana-rust-module-boundaries`
- `montana-rust-testing-patterns`
- `montana-pattern-regression-bugfix`
- `montana-pattern-conditional-rendering`

## Consistency contract (non-negotiables)
- Discover repo rules before editing; do not substitute personal defaults when the repo already specifies behavior.
- Prefer the smallest diff that solves the request while preserving existing architecture and public contracts.
- Verify the change with the narrowest meaningful checks first, then widen only when useful.
- Treat bugfixes as incomplete unless verification or regression coverage is addressed or explicitly blocked.
- Report what changed, what was verified, and what remains blocked in a stable, concise format.

## Montana defaults
Apply these when the repo does not already specify otherwise:
- Prefer explicit code over clever code.
- Prefer early returns over deep nesting.
- Prefer narrowly scoped helpers over broad abstractions.
- Prefer meaningful names over compressed names.
- Prefer boundary validation over optimistic assumptions about external data.

## Default workflow
1. Read the source-of-truth files and identify the smallest safe path forward.
2. Confirm the boundary affected: UI, API, service, persistence, or release surface.
3. Apply the smallest change that matches Montana preferences and repo conventions.
4. Run or attempt the narrowest useful verification command.
5. Report outcome, verification, and blockers in a consistent structure.

## Output format
- Request summary
- What changed
- Commands run
- Verification result
- Risks or blockers

## Safety rules
- Ask before broad refactors, public API changes, schema changes, dependency upgrades, or destructive actions.
- Never ask for secrets or request that they be pasted into prompts/logs.
- Stop and report when repo rules conflict with Montana defaults instead of silently choosing one.
