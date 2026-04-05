---
name: montana-rust-module-boundaries
description: Rust decision-spec skill for Montana choices around module layout, visibility, re-exports, and public-vs-internal API surfaces.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-rust","montana-rust-error-patterns","montana-backend-architecture","montana-usecase-delivery","montana-intake"]}}
---

Use this skill when Rust work involves organizing modules, exposing types/functions, choosing re-exports, or deciding what should remain internal.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-rust`
- `montana-rust-error-patterns`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-intake`

## Consistency contract (non-negotiables)
- Default to the narrowest visibility that supports the use case.
- Keep public surfaces intentional and reviewable.
- Prefer module structures that make ownership and API boundaries obvious.

## Montana preferred choices
- Prefer `pub(crate)` over `pub` unless a wider API is required.
- Prefer explicit re-exports from a clear boundary module when presenting a curated public surface.
- Prefer small, purpose-driven modules over oversized mixed-responsibility modules.
- Prefer internal helper modules/functions to remain private unless reuse or boundary design requires exposure.
- Prefer module organization that follows responsibility boundaries, not arbitrary file splits.

## Avoid / anti-patterns
- Marking items `pub` by default.
- Re-exporting large surfaces without intentional curation.
- Creating deep module hierarchies with no clear ownership benefit.
- Splitting one cohesive responsibility across many tiny files just to reduce line count.

## Decision table
- When only the current crate needs access, prefer `pub(crate)` or private visibility.
- When a crate-level API should be curated, re-export a small intentional surface from a boundary module.
- When a helper is local to one module, keep it private.
- When a module mixes unrelated responsibilities, split by boundary or responsibility, not by arbitrary syntax type.

## Default workflow
1. Identify what API surface is truly needed.
2. Reduce visibility to the narrowest correct scope.
3. Curate re-exports only where they improve the crate surface.
4. Keep modules aligned with responsibility boundaries.
5. Verify compile/test impact after visibility changes.

## Output format
- Module boundary affected
- Visibility decision
- Commands run
- API surface notes

## Safety rules
- Ask before widening public crate APIs or reorganizing many modules.
- Avoid broad module churn bundled with unrelated fixes.
- Stop and report if the repo has an explicit module convention that differs from Montana defaults.
