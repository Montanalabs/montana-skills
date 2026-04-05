---
name: montana-ts-runtime-validation
description: TypeScript decision-spec skill for validating external data at boundaries and keeping runtime behavior aligned with the type system.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-ts","montana-ts-style-decisions","montana-react","montana-backend-architecture","montana-frontend-architecture","montana-usecase-delivery"]}}
---

Use this skill when TypeScript code touches external input such as API payloads, environment variables, form data, query params, local storage, or untyped library results.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-ts`
- `montana-ts-style-decisions`
- `montana-react`
- `montana-backend-architecture`
- `montana-frontend-architecture`
- `montana-usecase-delivery`

## Consistency contract (non-negotiables)
- Treat external input as untrusted until validated or narrowed at a boundary.
- Keep runtime validation logic close to the boundary where untyped data enters the system.
- Do not use TypeScript annotations alone as a substitute for runtime validation.

## Montana preferred choices
- Prefer validating at the edge: API clients, handlers, env/config loaders, form adapters, or storage adapters.
- Prefer narrow, explicit checks that map data into trusted internal shapes.
- Prefer converting uncertain input into domain-safe values before passing it deeper into the system.
- Prefer failing fast with actionable error messages when invalid input is encountered.
- Prefer reusable validators only when the same shape recurs across boundaries.

## Avoid / anti-patterns
- Casting raw API or storage data directly to trusted app types.
- Spreading validation logic across many downstream consumers.
- Using `as SomeType` to hide missing runtime checks.
- Delaying validation until far inside business logic.

## Decision table
- When data comes from outside the repo boundary, validate or narrow it immediately.
- When the same external shape appears in multiple places, extract a shared boundary validator.
- When a value is optional externally but required internally, normalize it at the boundary.
- When invalid input should stop the flow, fail early with context instead of carrying partial data.

## Default workflow
1. Identify every external input in the requested change.
2. Place validation or normalization at the first boundary that receives the data.
3. Convert validated input into trusted internal types.
4. Keep deeper layers free from repeated defensive checks unless the boundary is ambiguous.
5. Verify typecheck and any tests affected by boundary behavior.

## Output format
- Boundary validated
- Validation approach chosen
- Commands run
- Runtime safety notes

## Safety rules
- Ask before introducing a new validation library or broad schema layer.
- Avoid repo-wide validation rewrites bundled with unrelated feature work.
- If the repo already has a validation strategy, follow it and report any Montana-preference difference.
