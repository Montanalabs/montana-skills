---
name: montana-js
description: JavaScript workflow helper: Node tooling, lint/format/test, debugging, and safe refactors.
metadata: {"montana":{"category":"language","composesWith":["montana-global-contract","montana-react","montana-frontend-architecture","montana-backend-architecture","montana-usecase-delivery","montana-intake","montana-pattern-regression-bugfix"]}}
---

Use this skill when working on JavaScript codebases (Node or browser), fixing runtime/test failures, or performing safe refactors.

## Category
- Language

## Works with
- `montana-global-contract`
- `montana-react`
- `montana-frontend-architecture`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-intake`
- `montana-pattern-regression-bugfix`

## Consistency contract (non-negotiables)
- Follow repo scripts/configs first (`package.json` scripts, eslint/prettier, test runner).
- Always lint/format/tests when available (or report exactly what blocks you).
- Keep diffs minimal and scoped to the request.
- Avoid introducing new dependencies unless explicitly approved.

## Default workflow
1. Identify the project scripts:
   - Inspect `package.json` scripts and the repo README.
2. Reproduce:
   - run the smallest command that reproduces the issue (test, build, dev)
3. Apply the smallest change
4. Run lint/format/test (repo-dependent)

## Commands (common; prefer repo scripts)
- Install: `npm ci` (or `pnpm i` / `yarn install`)
- Lint: `npm run lint`
- Format: `npm run format`
- Tests: `npm test` / `npm run test`
- Build: `npm run build`
- Dev: `npm run dev`

## Montana JavaScript standards (portable defaults)
Apply these when the repo doesn’t already specify otherwise:
- **Modules**: prefer ESM where possible; don’t mix ESM/CJS without need.
- **Async**: prefer `async/await` over raw promise chains for readability.
- **Errors**: don’t swallow errors; include actionable messages; avoid bare `catch {}`.
- **Docs**: add JSDoc for exported functions/classes when behavior isn’t obvious.
- **Testing**: add regression tests for bugfixes; keep tests deterministic.
JSDoc template: `{baseDir}/templates/jsdoc-exported.md`.
Additional templates:
- Node module patterns: `{baseDir}/templates/node-module-patterns.md`
- Error handling: `{baseDir}/templates/error-handling.md`

## Refactor rules
- Prefer small diffs and behavior-preserving changes.
- Keep changes consistent with existing style (ESM vs CJS, lint rules, formatting).
- Avoid introducing new dependencies unless asked.

## Output format
- **What changed**: files touched
- **Commands run**: and results
- **Why**: short explanation
- **Next steps**: optional follow-ups

## Safety rules
- Never request secrets or paste tokens into prompts/logs.
- Ask before doing repo-wide formatting or large renames.
- If lint/format/tests fail, stop and report the smallest actionable log excerpt plus the next fix to try.
