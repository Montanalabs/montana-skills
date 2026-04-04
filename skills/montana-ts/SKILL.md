---
name: montana-ts
description: TypeScript workflow helper: typecheck, lint/format, safe refactors, and migrations.
metadata: {"montana":{"category":"language","composesWith":["montana-react","montana-frontend-architecture","montana-backend-architecture","montana-usecase-delivery","montana-intake"]}}
---

Use this skill when working on TypeScript code, fixing type errors, refactoring safely, or doing dependency/tooling migrations with explicit approval.

## Category
- Language

## Works with
- `montana-react`
- `montana-frontend-architecture`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-intake`

## Consistency contract (non-negotiables)
- Follow repo scripts/configs first (`package.json` scripts, eslint/prettier/tsconfig).
- Always typecheck + lint + tests when available (or report exactly what blocks you).
- Keep diffs minimal and scoped to the request.
- Public API changes require explicit confirmation.

## Default workflow
1. Identify the project setup:
   - `package.json` scripts, `tsconfig*.json`, bundler (Vite/Next/etc)
2. Reproduce:
   - run the smallest typecheck/build/test that reproduces the issue
3. Apply the smallest change
4. Run formatting/linting (only what the repo uses)
5. Re-run typecheck/tests

## Commands (common; follow repo scripts first)
- Install: `npm ci` (or `pnpm i`, `yarn install` per repo)
- Typecheck: `npm run typecheck` or `tsc -p tsconfig.json --noEmit`
- Lint: `npm run lint`
- Format: `npm run format`
- Tests: `npm test` / `npm run test` / `vitest` / `jest` (repo-dependent)

## Montana TypeScript standards (portable defaults)
Apply these when the repo doesn’t already specify otherwise:
- **Exports**: prefer named exports; avoid default exports for shared modules.
- **Types**: avoid `any`; prefer `unknown` + narrowing when necessary.
- **Nullability**: don’t “type away” `null`/`undefined`; fix the data flow or narrow explicitly.
- **Docs**: add JSDoc for exported functions/classes (purpose, params, returns, throws when relevant).
- **Errors**: throw `Error` (or project-specific types); include actionable messages; don’t swallow errors silently.
- **API boundaries**: validate external inputs at the boundary (runtime checks) when appropriate for the app.
JSDoc template: `{baseDir}/templates/jsdoc-exported.md`.
Additional templates:
- Module boundaries: `{baseDir}/templates/module-boundary.md`
- Runtime validation: `{baseDir}/templates/runtime-validation.md`
- Migration plan: `{baseDir}/templates/migration-plan.md`

## Refactor rules
- Prefer mechanical refactors (rename symbol, extract function) with minimal behavior change.
- Avoid `any` unless it’s a deliberate escape hatch with a follow-up plan.
- Don’t change public APIs without confirmation.
- Keep types aligned with runtime behavior (don’t “type away” null/undefined risks).

## Migration rules (high-risk)
If asked to migrate tooling (eslint changes, TS major version, bundler changes):
- First produce a plan and list expected churn.
- Ask for confirmation before making broad dependency upgrades or repo-wide formatting.

## Output format
- **What changed**: files touched
- **Commands run**: and results
- **Why it works**: short explanation
- **Next steps**: optional follow-ups

## Safety rules
- Never ask for secrets or paste them into configs.
- Avoid surprise lockfile churn unless necessary and explained.
- If typecheck/lint/tests fail, stop and report the smallest actionable log excerpt plus the next fix to try.
