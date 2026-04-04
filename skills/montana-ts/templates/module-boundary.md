# TypeScript module boundary rules (Montana defaults)

## Defaults
- Enforce clear boundaries: “feature modules” should not import from each other’s internals.
- Public surface area should live in an `index.ts` (barrel) or explicitly exported entry.
- Avoid deep relative imports that bypass public APIs (e.g., `../feature/internal/*`).

