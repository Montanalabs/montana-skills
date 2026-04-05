# Case: `montana-ts-error-patterns`

## Skill under test

`montana-ts-error-patterns`

## Fixture

`tests/skill-eval/fixtures/js-node-service`

## Prompt

Model the job-runner failure path so errors are actionable, not swallowed, and can be surfaced at the right boundary without leaking unhelpful internals.

## Scoring rubric

- `actionable error handling`: 4 points
- `no swallowed failures`: 2 points
- `boundary-aware mapping`: 2 points
- `clear catch-narrowing/reporting`: 2 points

## Expected commands

- read job runner source and scripts

## Expected boundaries

- no silent catch path
- preserve useful context
- avoid raw string throw patterns

## Red flags

- catch and ignore
- generic `"something went wrong"` with no context
- leaking irrelevant lower-level details upward

## Transcript

`tests/skill-eval/transcripts/codex/montana-ts-error-patterns.md`
