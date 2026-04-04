---
name: montana-intake
description: Fast project intake: identify stack, commands, tests, structure, and a safe next-step plan.
metadata: {"montana":{"category":"intake","composesWith":["montana-rust","montana-go","montana-py","montana-ts","montana-js","montana-react","montana-frontend-architecture","montana-backend-architecture","montana-usecase-delivery","montana-release"],"recommendedWith":["montana-usecase-delivery"]}}
---

Use this skill when starting in an unfamiliar repo, before making changes, or when the user says “help me get oriented”.

## Category
- Intake

## Works with
- `montana-rust`
- `montana-go`
- `montana-py`
- `montana-ts`
- `montana-js`
- `montana-react`
- `montana-frontend-architecture`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-release`

## Consistency contract (what this skill sets up)
The goal is to make agent work **consistent across developers** by:
- discovering the repo’s “source of truth” commands (format/lint/test/build)
- identifying architecture/conventions that must be followed
- producing a concrete “definition of done” for future agent work

## Goals
- Produce a short, accurate map of the project (tech, folders, build/test commands).
- Identify the safest way to reproduce an issue (or run checks) before editing.
- Ask only the *minimum* clarifying questions needed to proceed.

## Default workflow
1. Identify the runtime + language(s) and the primary entrypoints:
   - Check `README.md`, `package.json`, build files, and top-level folders.
2. Identify the **golden commands** (prefer what the repo documents):
   - install deps
   - typecheck/lint/format
   - unit/integration tests
   - build
   - dev server
3. Identify the project structure:
   - where “app code” lives
   - where tests live
   - where configs live
   - what the architecture boundaries are (features/modules/layers)
4. Identify risks before changing code:
   - monorepo vs single package
   - generated code
   - pinned tool versions
   - formatting/linting rules that must not be violated
5. Output an “action plan” for the user’s request:
   - smallest next step you can do safely
   - what you need from the user (if anything)
   - definition of done (format/lint/test must pass)
If you need templates:
- Definition of done: `{baseDir}/templates/definition-of-done.md`
- Conventions discovery: `{baseDir}/templates/project-conventions.md`
- Minimal questions: `{baseDir}/templates/question-set.md`

## Output format
Return a concise report:
- **Stack**: languages/frameworks/build tools
- **Key folders**: short descriptions
- **Commands**: install / test / lint / build / dev (as applicable)
- **Conventions**: formatting/lint/type rules + doc expectations (as discovered)
- **Next steps**: 3–6 bullets
- **Questions (if blocked)**: 0–3 targeted questions

## Safety rules
- Do not run destructive commands (`rm -rf`, rewriting history, publishing) without explicit confirmation.
- Do not request secrets. Never ask the user to paste tokens/keys.
- Prefer “read-only” discovery first (docs + file listing + grep).
