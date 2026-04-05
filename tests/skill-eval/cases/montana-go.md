# Case: `montana-go`

## Skill under test

`montana-go`

## Fixture

`tests/skill-eval/fixtures/go-api`

## Prompt

Fix the failing user service test, run formatting, and re-run the smallest useful test command before widening.

## Scoring rubric

- `focused reproduction and retest`: 4 points
- `gofmt discipline`: 2 points
- `minimal regression-oriented fix`: 2 points
- `clear blocker reporting`: 2 points

## Expected commands

- `go test ./internal/service` or equivalent focused test
- `gofmt -w` on changed files
- cache workaround reporting if the sandbox blocks default Go cache usage

## Expected boundaries

- should fix the whitespace validation issue without dependency churn
- should widen test scope only after the local failure is addressed
- should keep the diff local to the affected package

## Red flags

- repo-wide changes
- dependency edits
- skipping format/test reporting

## Transcript

`tests/skill-eval/transcripts/codex/montana-go.md`
