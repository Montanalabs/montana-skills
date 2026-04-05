# Case: `montana-go-service-patterns`

## Skill under test

`montana-go-service-patterns`

## Fixture

`tests/skill-eval/fixtures/go-api`

## Prompt

Refactor the create-user flow so transport-specific validation stays in the handler, business logic stays in the service, and interfaces live near the consumer that needs them.

## Scoring rubric

- `service/handler split`: 4 points
- `consumer-owned interface choice`: 2 points
- `minimal structural churn`: 2 points
- `clear layer reporting`: 2 points

## Expected commands

- read handler and service files
- focused `go test` if environment allows

## Expected boundaries

- business rules in service
- transport parsing/validation in handler
- no unnecessary interface creation

## Red flags

- business logic in handlers
- interface added “just in case”
- request object passed deep into services

## Transcript

`tests/skill-eval/transcripts/codex/montana-go-service-patterns.md`
