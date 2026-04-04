---
name: montana-release
description: Release helper: produce changelog + release notes and a safe, confirmation-first release checklist.
metadata: {"montana":{"category":"use-case","composesWith":["montana-usecase-delivery","montana-intake","montana-rust","montana-go","montana-py","montana-ts","montana-js","montana-frontend-architecture","montana-backend-architecture"]}}
---

Use this skill when preparing a public release: changelog entries, release notes, and a safe “what to run” checklist.

## Category
- Use-case

## Works with
- `montana-usecase-delivery`
- `montana-intake`
- `montana-rust`
- `montana-go`
- `montana-py`
- `montana-ts`
- `montana-js`
- `montana-frontend-architecture`
- `montana-backend-architecture`

## Consistency contract (non-negotiables)
- Never publish/tag/push without explicit user confirmation.
- Prefer the repo’s documented release process; don’t guess.
- Output must be copy/pasteable and reviewable (markdown + commands).

## Inputs
Provide one or more of:
- A version number (or “patch/minor/major” intent)
- A list of merged PRs/commits or a diff summary
- The release platform (GitHub Releases, npm, crates.io, PyPI, etc.)

## Default workflow
1. Determine current versioning system:
   - Look for `CHANGELOG.md`, `package.json`, `Cargo.toml`, `go.mod`, `pyproject.toml`, tags, or documented policy.
2. Summarize changes into user-facing categories:
   - Added / Changed / Fixed / Security / Breaking
3. Draft:
   - Changelog entry
   - Release notes (short, public-friendly)
4. Produce a **confirmation-first** release checklist:
   - tests, build artifacts, signing, tagging, publishing steps
   - explicitly mark steps that are destructive/irreversible
Templates:
- Changelog: `{baseDir}/templates/changelog-entry.md`
- Release notes: `{baseDir}/templates/release-notes.md`
- Checklist: `{baseDir}/templates/release-checklist.md`

## Output format
- **Proposed version**: and rationale (if applicable)
- **Changelog entry**: markdown
- **Release notes**: markdown
- **Release checklist**: step-by-step commands (where possible)
- **Questions**: only if needed to avoid mistakes

## Safety rules
- Never publish, tag, or push without explicit user confirmation.
- Never request secrets (tokens, API keys). If publishing requires credentials, say “ensure credentials are configured” without asking for them.
- Avoid guessing release commands; prefer the repo’s documented release process if present.
