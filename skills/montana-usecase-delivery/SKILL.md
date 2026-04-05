---
name: montana-usecase-delivery
description: Use-case delivery skill for turning product requests into scoped implementation plans, acceptance criteria, and verifiable outcomes.
metadata: {"montana":{"category":"use-case","composesWith":["montana-global-contract","montana-intake","montana-rust","montana-go","montana-py","montana-ts","montana-js","montana-react","montana-frontend-architecture","montana-backend-architecture","montana-ts-style-decisions","montana-ts-runtime-validation","montana-ts-error-patterns","montana-react-rendering-patterns","montana-react-state-ownership","montana-react-form-patterns","montana-go-service-patterns","montana-go-http-boundaries","montana-go-testing-patterns","montana-rust-error-patterns","montana-rust-module-boundaries","montana-rust-testing-patterns","montana-pattern-regression-bugfix","montana-pattern-conditional-rendering"]}}
---

Use this skill when the agent needs to translate a feature request or bug report into a well-scoped implementation with a clear definition of done.

## Category
- Use-case

## Works with
- `montana-global-contract`
- `montana-intake`
- `montana-rust`
- `montana-go`
- `montana-py`
- `montana-ts`
- `montana-js`
- `montana-react`
- `montana-frontend-architecture`
- `montana-backend-architecture`
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
- Convert requests into explicit scope, assumptions, risks, and acceptance criteria.
- Keep implementation aligned with the smallest deliverable that solves the request.
- Define what verification is required before the task is considered done.

## Montana defaults
Apply these when the repo does not already specify otherwise:
- Always restate expected behavior in concrete terms.
- Identify in-scope vs out-of-scope changes.
- Add regression coverage for bugfixes when feasible.
- Include rollback or follow-up notes when risk is non-trivial.

## Default workflow
1. Restate the request as a concrete use-case.
2. Identify affected surfaces: UI, API, storage, tests, docs, release notes.
3. Define acceptance criteria.
4. Implement the smallest valid change.
5. Verify and report outcomes against the acceptance criteria.

## Output format
- Request summary
- Scope and assumptions
- Acceptance criteria
- What changed
- Commands run
- Risks / follow-ups

## Safety rules
- Ask before expanding scope beyond the user’s request.
- Ask before bundling refactors with feature work.
- Stop if the request is ambiguous enough to risk incorrect behavior and report the missing fact.

## Templates
- Use `{baseDir}/templates/acceptance-criteria.md`
- Use `{baseDir}/templates/implementation-plan.md`
- Use `{baseDir}/templates/bugfix-template.md`
