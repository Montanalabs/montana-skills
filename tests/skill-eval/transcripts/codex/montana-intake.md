# Codex Transcript: `montana-intake`

## Outcome

Pass with moderate confidence.

## What Codex did

- inspected the fixture `README.md`, `package.json`, and `tsconfig.json`
- identified the stack as React + TypeScript + Vite-style scripts
- mapped `src/features` and `src/shared` as the main structural boundaries
- surfaced the golden commands from the fixture without inventing extras

## Commands attempted

- `rg --files`
- `sed -n '1,200p' README.md`
- `sed -n '1,200p' package.json`
- `sed -n '1,200p' tsconfig.json`

## Assessment

The intake guidance lines up well with this fixture. The strongest behavior is repo-first discovery before proposing changes.
