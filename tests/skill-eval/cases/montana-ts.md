# Case: `montana-ts`

## Skill under test

`montana-ts`

## Fixture

`tests/skill-eval/fixtures/ts-react-app`

## Prompt

Fix the TypeScript issue around nullable API data in the cart feature with the smallest safe change, then run the repo checks you can.

## Scoring rubric

- `nullability fix quality`: 4 points
- `repo-script-first verification`: 2 points
- `minimal diff`: 2 points
- `no unsafe typing escape hatches`: 2 points

## Expected commands

- inspection of `package.json`, `tsconfig.json`, and cart files
- `npm run typecheck` if dependencies are available
- fallback reporting if runtime checks cannot execute

## Expected boundaries

- should not use `any`
- should not hide the issue with a type assertion
- should keep the change local to the cart feature

## Red flags

- using `any`
- forcing non-null with no runtime guard
- changing unrelated frontend code

## Transcript

`tests/skill-eval/transcripts/codex/montana-ts.md`
