# Case: `montana-go-http-boundaries`

## Skill under test

`montana-go-http-boundaries`

## Fixture

`tests/skill-eval/fixtures/go-api`

## Prompt

Refactor the create-user endpoint so `http.Request` stays at the transport edge and the service receives only domain-safe inputs.

## Scoring rubric

- `request stays at edge`: 4 points
- `transport/domain mapping clarity`: 3 points
- `status/error mapping discipline`: 2 points
- `minimal change scope`: 1 point

## Expected commands

- read HTTP handler and service files
- narrow `go test` if possible

## Expected boundaries

- parse/validate in handler
- domain-safe params into service
- map domain/service errors back at handler boundary

## Red flags

- passing `*http.Request` into service
- HTTP status concerns leaking into service
- broad handler framework churn

## Transcript

`tests/skill-eval/transcripts/codex/montana-go-http-boundaries.md`
