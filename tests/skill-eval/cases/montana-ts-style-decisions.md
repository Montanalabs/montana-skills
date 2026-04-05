# Case: `montana-ts-style-decisions`

## Skill under test

`montana-ts-style-decisions`

## Fixture

`tests/skill-eval/fixtures/ts-react-app`

## Prompt

Refactor the cart feature so the exported helper stays a function declaration, nullable API data is handled without assertions, and no enum is introduced for app-owned states.

## Scoring rubric

- `preferred TS choices applied`: 4 points
- `nullability handled safely`: 2 points
- `no style drift`: 2 points
- `minimal local change`: 2 points

## Expected commands

- read `package.json`, `tsconfig.json`, and cart files
- repo-script discovery for typecheck

## Expected boundaries

- prefer function declarations for exported utilities
- avoid `any`, non-null assertions, and unnecessary enums
- keep the change local to the cart feature

## Red flags

- introducing enums for local app state
- hiding the issue with a cast or assertion
- broad stylistic rewrites

## Transcript

`tests/skill-eval/transcripts/codex/montana-ts-style-decisions.md`
