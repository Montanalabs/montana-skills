---
name: montana-ts-style-decisions
description: TypeScript decision-spec skill for choosing consistent Montana patterns around functions, type modeling, exports, constants, and null handling.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-ts","montana-react","montana-frontend-architecture","montana-backend-architecture","montana-usecase-delivery"]}}
---

Use this skill when a TypeScript task has multiple valid implementation options and you want the Montana-preferred choice.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-ts`
- `montana-react`
- `montana-frontend-architecture`
- `montana-backend-architecture`
- `montana-usecase-delivery`

## Consistency contract (non-negotiables)
- Prefer the same TypeScript shape for the same problem type across repos unless the repo already mandates otherwise.
- Do not use `any` as a convenience escape hatch.
- Keep runtime behavior aligned with the type model; never "type away" real nullability or boundary risk.

## Montana preferred choices
- Prefer named exports over default exports for shared modules.
- Prefer function declarations for exported pure utilities and module-level helpers.
- Prefer arrow functions for inline callbacks, closures, React-local handlers, and small non-exported helpers.
- Prefer string literal unions over enums unless interoperating with external schemas, generated code, or runtime enum requirements.
- Prefer named constants only when a value is reused, semantically meaningful, or part of a boundary contract.
- Prefer inline literals when the value is local, obvious, and used once.
- Prefer `unknown` plus narrowing over `any`.
- Prefer explicit narrowing or defaulting over non-null assertions.

## Avoid / anti-patterns
- Exporting many default exports from shared modules.
- Introducing enums for app-owned string domains without a runtime need.
- Creating constants for every string or number regardless of reuse or meaning.
- Using type assertions to skip real data-flow fixes.

## Default workflow
1. Identify which TypeScript decision surface is in play: export shape, function form, type modeling, constants, or nullability.
2. Check whether the repo already chooses differently.
3. Apply the Montana-preferred choice only where it improves consistency and does not create churn.
4. Verify typecheck impact and call out any behavior-sensitive choice.

## Decision table
- When defining an exported pure utility, prefer a function declaration.
- When defining an inline callback or React-local handler, prefer an arrow function.
- When modeling an app-owned fixed string set, prefer a string literal union.
- When handling nullable API data, prefer narrowing, fallback values, or boundary validation over assertions.
- When a literal is single-use and obvious, keep it inline instead of extracting a constant.

## Output format
- Decision surface involved
- Choice made and why
- Commands run
- Type or runtime notes

## Safety rules
- Ask before repo-wide style conversions.
- Ask before changing exported API types in a way that can affect consumers.
- If the repo clearly uses a different convention, follow the repo and report the Montana divergence.
