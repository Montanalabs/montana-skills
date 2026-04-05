---
name: montana-ts-error-patterns
description: TypeScript decision-spec skill for Montana error handling, actionable messages, boundary-safe propagation, and consistent failure modeling.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-ts","montana-ts-style-decisions","montana-ts-runtime-validation","montana-react","montana-backend-architecture","montana-usecase-delivery","montana-pattern-regression-bugfix"]}}
---

Use this skill when TypeScript work involves throwing, catching, mapping, or presenting errors and multiple valid error-handling styles are possible.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-ts`
- `montana-ts-style-decisions`
- `montana-ts-runtime-validation`
- `montana-react`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-pattern-regression-bugfix`

## Consistency contract (non-negotiables)
- Errors should be actionable, explicit, and aligned with the boundary the caller understands.
- Do not swallow errors silently or hide them behind generic type assertions.
- Keep TypeScript error handling consistent across frontend and backend work unless the repo already defines a different contract.

## Montana preferred choices
- Prefer throwing `Error` or project-specific error classes/types instead of raw strings.
- Prefer mapping low-level failures into caller-meaningful errors at boundaries.
- Prefer `unknown` in `catch` blocks and narrow before use.
- Prefer preserving useful context while avoiding leaking irrelevant internals across boundaries.
- Prefer returning structured failure states in UI-facing flows when the caller needs to branch without exceptions.

## Avoid / anti-patterns
- `catch {}` with no reporting or rethrow.
- Throwing arbitrary strings or mixed shapes.
- Leaking storage, HTTP, or third-party details directly into higher-level app errors without intent.
- Converting real failures into silent fallbacks unless the fallback is an explicit product behavior.

## Decision table
- When catching an error in TypeScript, treat it as `unknown` and narrow it explicitly.
- When the caller needs actionable handling, map the failure into a stable domain or UI-meaningful shape.
- When an error crosses a major boundary, add context rather than passing a vague message upward.
- When UI state needs to render failure meaningfully, prefer explicit error state over swallowed exceptions.

## Default workflow
1. Identify the boundary where the error originates and the boundary where it is consumed.
2. Choose a failure shape the caller can understand.
3. Preserve useful context without leaking irrelevant implementation details.
4. Verify the failure path through targeted tests or narrow reproduction.

## Output format
- Error boundary affected
- Pattern chosen
- Commands run
- Failure-path notes

## Safety rules
- Ask before changing public error contracts or introducing a new error abstraction repo-wide.
- Avoid bundling broad error rewrites with unrelated work.
- If the repo already has a stable error model, follow it and report the Montana divergence if needed.
