---
name: montana-frontend-architecture
description: Frontend architecture skill for feature structure, UI boundaries, state ownership, and maintainable client-side code.
metadata: {"montana":{"category":"architecture","composesWith":["montana-ts","montana-js","montana-react","montana-usecase-delivery"]}}
---

Use this skill when the agent needs to shape or preserve the structure of a frontend application.

## Category
- Architecture

## Works with
- `montana-ts`
- `montana-js`
- `montana-react`
- `montana-usecase-delivery`

## Consistency contract (non-negotiables)
- Separate UI rendering, domain logic, and data access concerns.
- Organize code by feature or domain, not by arbitrary file type alone.
- Avoid cross-feature imports into internal modules.
- Keep network and persistence concerns at defined boundaries.

## Montana defaults
Apply these when the repo does not already specify otherwise:
- Prefer feature-oriented directories.
- Keep shared UI primitives separate from feature-specific UI.
- Place API clients, adapters, or gateway code behind stable interfaces.
- Keep validation at the edges: forms, server responses, environment/config.

## Default workflow
1. Identify the current frontend structure and its boundary rules.
2. Determine whether the requested change belongs to an existing feature or a new one.
3. Add or update code in the narrowest layer possible.
4. Verify imports, state ownership, and API boundaries remain clean.
5. Report the structural impact.

## Output format
- What changed
- Feature/module boundaries affected
- Commands run
- Architecture notes

## Safety rules
- Ask before broad folder reorganizations.
- Ask before introducing new shared abstractions.
- Stop if the requested change conflicts with the repo’s existing architecture and report the tradeoff.

## Templates
- Use `{baseDir}/templates/feature-module-template.md`
- Use `{baseDir}/templates/state-ownership-checklist.md`
- Use `{baseDir}/templates/ui-boundaries.md`
