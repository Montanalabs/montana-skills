# Case: `montana-js`

## Skill under test

`montana-js`

## Fixture

`tests/skill-eval/fixtures/js-node-service`

## Prompt

Fix the error handling in the job runner so failures are logged with context and the process exits non-zero instead of silently continuing.

## Scoring rubric

- `error-handling quality`: 4 points
- `node-style consistency`: 2 points
- `verification behavior`: 2 points
- `no dependency churn`: 2 points

## Expected commands

- inspection of `package.json` and `src/jobRunner.js`
- `npm test` if dependencies are available
- clear blocker reporting if the environment cannot run full checks

## Expected boundaries

- should preserve ESM module style
- should keep the fix within the existing runner flow
- should surface actionable error context

## Red flags

- swallowing errors
- changing module format without need
- adding packages

## Transcript

`tests/skill-eval/transcripts/codex/montana-js.md`
