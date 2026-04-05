# Case: `montana-go-testing-patterns`

## Skill under test

`montana-go-testing-patterns`

## Fixture

`tests/skill-eval/fixtures/go-api`

## Prompt

Choose the smallest useful Go test strategy for the whitespace-only user-name bug, preferring a focused regression-oriented package test over unnecessary breadth.

## Scoring rubric

- `focused test choice`: 4 points
- `regression-test mindset`: 2 points
- `layer-appropriate test shape`: 2 points
- `clear widening strategy`: 2 points

## Expected commands

- focused package test command
- `gofmt -w` if edits are made

## Expected boundaries

- prefer package-level or direct boundary tests before `./...`
- use clear fakes/tables only when they help
- widen only after local confirmation

## Red flags

- immediate broad test run
- unclear or overcomplicated test structure
- no regression framing

## Transcript

`tests/skill-eval/transcripts/codex/montana-go-testing-patterns.md`
