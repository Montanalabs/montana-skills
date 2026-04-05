---
name: montana-go-testing-patterns
description: Go decision-spec skill for Montana testing choices: focused reproduction, table-driven tests, boundary tests, and regression-oriented verification.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-go","montana-go-service-patterns","montana-go-http-boundaries","montana-backend-architecture","montana-usecase-delivery","montana-pattern-regression-bugfix"]}}
---

Use this skill when Go tasks involve choosing test shape, granularity, and reproduction strategy.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-go`
- `montana-go-service-patterns`
- `montana-go-http-boundaries`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-pattern-regression-bugfix`

## Consistency contract (non-negotiables)
- Prefer the smallest focused test that proves the behavior at issue.
- Treat regression coverage as part of the bugfix path when the repo supports it.
- Keep Go tests readable, table-driven where that clarifies branching, and aligned with the layer under test.

## Montana preferred choices
- Prefer focused package tests before widening to `./...`.
- Prefer table-driven tests for pure branching or many input/output cases.
- Prefer direct boundary tests for handlers, services, and adapters rather than broad integration setup when the bug is local.
- Prefer test fixtures/fakes that make the failure reason obvious.
- Prefer adding a regression case before or alongside the fix when practical.

## Avoid / anti-patterns
- Jumping directly to broad repo-wide test runs when a narrow package test exists.
- Table-driven tests that are harder to read than the logic they cover.
- Over-mocking when a simple fake or direct test would be clearer.
- Fixing a bug without adding a focused regression case when the repo can support one.

## Decision table
- When the behavior is local to one package, start with that package test.
- When many branch cases exist, prefer a table-driven test.
- When HTTP boundary behavior is at issue, test the handler boundary directly.
- When service behavior depends on collaborators, use simple fakes at the consumer boundary.

## Default workflow
1. Reproduce with the narrowest package/test target.
2. Choose the simplest test shape that clarifies the behavior.
3. Add or update regression coverage.
4. Re-run focused tests, then widen if useful.
5. Report the exact verification path.

## Output format
- Test strategy chosen
- Scope of verification
- Commands run
- Regression coverage notes

## Safety rules
- Ask before replacing the repo’s test style or introducing a new testing helper pattern broadly.
- Avoid sweeping test rewrites bundled with unrelated code fixes.
- If the environment blocks test execution, report the blocker and the narrowest fallback evidence.
