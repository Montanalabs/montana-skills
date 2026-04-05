---
name: montana-rust-testing-patterns
description: Rust decision-spec skill for Montana test strategy: focused reproduction, unit-vs-boundary testing, regression coverage, and clear failure surfaces.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-rust","montana-rust-error-patterns","montana-rust-module-boundaries","montana-backend-architecture","montana-usecase-delivery","montana-pattern-regression-bugfix"]}}
---

Use this skill when Rust work involves choosing what to test, how broadly to verify, and how to add durable regression coverage.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-rust`
- `montana-rust-error-patterns`
- `montana-rust-module-boundaries`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-pattern-regression-bugfix`

## Consistency contract (non-negotiables)
- Prefer the narrowest test that proves the bug or requirement.
- Add regression protection when a bugfix changes observable behavior.
- Keep Rust tests explicit about the boundary or contract they validate.

## Montana preferred choices
- Prefer focused unit tests for pure logic and parser/transform behavior.
- Prefer boundary tests when the bug lives at a public API, adapter, or module surface.
- Prefer small targeted test cases that describe the failure clearly.
- Prefer checking meaningful failure behavior rather than only "it does not panic."
- Prefer widening to broader `cargo test` scope after the local fix is confirmed.

## Avoid / anti-patterns
- Only running broad tests when a single focused test would reproduce the failure faster.
- Writing vague tests that do not reveal the intended contract.
- Treating "does not panic" as sufficient coverage for domain behavior.
- Skipping regression coverage when a concrete failing case can be expressed.

## Decision table
- When logic is pure and local, write a focused unit test.
- When visibility or surface behavior matters, test the boundary that the caller sees.
- When a bug can be expressed with one failing example, prefer a narrow regression test before broad expansion.
- When the local fix is confirmed, widen verification to broader test scope if practical.

## Default workflow
1. Reproduce with the smallest meaningful test target.
2. Decide whether the behavior belongs in a unit test or a boundary-oriented test.
3. Add regression coverage for the failure.
4. Re-run the focused test, then widen verification.
5. Report the test path clearly.

## Output format
- Test boundary chosen
- Regression case added or updated
- Commands run
- Verification notes

## Safety rules
- Ask before large test-module reorganizations.
- Avoid broad test refactors bundled with unrelated fixes.
- If the environment blocks full verification, report the focused evidence gathered and what remains unverified.
