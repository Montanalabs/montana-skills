---
name: montana-rust-error-patterns
description: Rust decision-spec skill for Montana error handling, visibility defaults, context propagation, and boundary error mapping.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-rust","montana-backend-architecture","montana-usecase-delivery","montana-intake"]}}
---

Use this skill when Rust tasks involve error design, propagation, boundary mapping, or public-vs-internal visibility choices tied to error surfaces.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-rust`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-intake`

## Consistency contract (non-negotiables)
- Prefer explicit, reviewable error flows over convenience shortcuts.
- Keep internal errors expressive without overexposing implementation details at public boundaries.
- Make Rust error handling look similar across tasks so agents converge on the same design.

## Montana preferred choices
- Prefer domain-specific error enums when callers need meaningful branching or boundary mapping.
- Prefer `pub(crate)` over `pub` unless the wider visibility is intentional.
- Prefer adding context when propagating errors across meaningful boundaries.
- Prefer mapping lower-level errors into domain or boundary errors instead of leaking dependency-specific details outward.
- Prefer `Result<T, E>` with meaningful error types over stringly typed errors when the error is part of the domain surface.

## Avoid / anti-patterns
- `unwrap()` or `expect()` in production paths.
- Public error surfaces that leak storage, HTTP, or third-party crate details without need.
- Using `String` errors where a stable domain error enum is justified.
- Making modules or types public by default without checking the intended surface.

## Default workflow
1. Identify whether the error is internal, domain-level, or boundary-facing.
2. Choose the narrowest visibility that still satisfies the use case.
3. Add context where the failure crosses an important boundary.
4. Map low-level errors at the boundary the caller understands.
5. Verify with focused tests or compile checks.

## Decision table
- When callers need to branch on the failure meaning, prefer a domain error enum.
- When an error is purely internal and not semantically important, propagation with context is usually enough.
- When choosing visibility, default to `pub(crate)` until a wider API is required.
- When moving from infrastructure to domain or API boundaries, map errors into caller-meaningful types/messages.

## Output format
- Error surface affected
- Error pattern chosen
- Commands run
- Boundary notes

## Safety rules
- Ask before changing public error types or widening visibility in a public API.
- Avoid mass error refactors bundled with unrelated work.
- If compile/tests fail, report the smallest actionable excerpt and the next fix to try.
