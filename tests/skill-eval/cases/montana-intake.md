# Case: `montana-intake`

## Skill under test

`montana-intake`

## Fixture

`tests/skill-eval/fixtures/ts-react-app`

## Prompt

Use the intake skill to orient yourself in this repo. Identify the stack, main folders, golden commands, constraints, and the safest next step before any code changes.

## Scoring rubric

- `repo mapping accuracy`: 4 points
- `golden commands match repo files`: 3 points
- `minimal-question behavior`: 2 points
- `safe next-step plan`: 1 point

## Expected commands

- `rg --files`
- `sed -n` or equivalent file reads
- inspection of `README.md`, `package.json`, and `tsconfig.json`

## Expected boundaries

- should stay read-only
- should derive scripts from the fixture instead of inventing them
- should summarize feature structure from `src/features` and `src/shared`

## Red flags

- inventing scripts that are not in `package.json`
- broad clarifying questions before reading the repo
- skipping constraints and definition-of-done thinking

## Transcript

`tests/skill-eval/transcripts/codex/montana-intake.md`
