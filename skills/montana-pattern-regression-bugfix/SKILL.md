---
name: montana-pattern-regression-bugfix
description: Pattern skill for Montana-style bugfix delivery: reproduce, isolate, fix narrowly, add regression coverage, and report the verified outcome.
metadata: {"montana":{"category":"pattern","composesWith":["montana-global-contract","montana-intake","montana-rust","montana-go","montana-py","montana-ts","montana-js","montana-react","montana-usecase-delivery","montana-go-service-patterns","montana-rust-error-patterns","montana-ts-runtime-validation","montana-react-state-ownership"]}}
---

Use this skill when fixing a bug and you want the solution path to be repeatable across agents.

## Category
- Pattern

## Works with
- `montana-global-contract`
- `montana-intake`
- `montana-rust`
- `montana-go`
- `montana-py`
- `montana-ts`
- `montana-js`
- `montana-react`
- `montana-usecase-delivery`
- `montana-go-service-patterns`
- `montana-rust-error-patterns`
- `montana-ts-runtime-validation`
- `montana-react-state-ownership`

## Preferred pattern
1. Reproduce the failure with the smallest meaningful command or direct assertion.
2. Identify the real boundary or decision that is failing.
3. Apply the narrowest fix that solves the bug without bundling unrelated cleanup.
4. Add or update regression coverage when the repo supports it.
5. Re-run the narrowest useful verification and report outcome clearly.

## Anti-patterns
- Fixing the symptom without reproducing the failure.
- Bundling stylistic refactors with the bugfix.
- Relying on type assertions or broad catches instead of addressing the real boundary problem.
- Declaring the bug fixed without verification or blocker reporting.

## Rationale
- Reproduction reduces guesswork.
- Narrow fixes reduce unintended regressions.
- Regression coverage turns one-time debugging into durable prevention.
- Stable reporting makes bugfix output more consistent between agents.

## Default workflow
1. Reproduce.
2. Isolate.
3. Fix narrowly.
4. Add regression protection.
5. Verify and report.

## Output format
- Bug reproduced by
- Root cause
- Narrow fix applied
- Regression coverage added or blocker noted
- Verification result

## Safety rules
- Ask before broad refactors, dependency upgrades, or contract changes during a bugfix.
- If regression coverage is not possible, explain why instead of silently skipping it.
- Stop and report when the bug cannot be reproduced with available repo tooling.
