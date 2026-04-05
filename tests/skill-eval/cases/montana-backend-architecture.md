# Case: `montana-backend-architecture`

## Skill under test

`montana-backend-architecture`

## Fixture

`tests/skill-eval/fixtures/go-api`

## Prompt

Move request validation and transport mapping into the handler and keep business rules in the service layer for the create-user flow.

## Scoring rubric

- `layering correctness`: 4 points
- `thin-handler behavior`: 2 points
- `persistence isolation`: 2 points
- `contract-impact reporting`: 2 points

## Expected commands

- inspection of `internal/http` and `internal/service`
- focused `go test` usage if environment allows

## Expected boundaries

- validation and HTTP-specific mapping in handler
- business rules in service
- repository details hidden behind interfaces

## Red flags

- business logic in handlers
- repository or transport concerns leaking upward
- public contract changes without warning

## Transcript

`tests/skill-eval/transcripts/codex/montana-backend-architecture.md`
