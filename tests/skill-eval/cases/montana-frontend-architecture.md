# Case: `montana-frontend-architecture`

## Skill under test

`montana-frontend-architecture`

## Fixture

`tests/skill-eval/fixtures/ts-react-app`

## Prompt

Refactor the cart feature so API access is behind a stable feature boundary instead of being imported directly into UI components.

## Scoring rubric

- `boundary improvement quality`: 4 points
- `feature-oriented structure`: 3 points
- `minimal churn`: 2 points
- `architecture reporting`: 1 point

## Expected commands

- inspection of feature folders and cart imports
- repo layout discovery via file listing and source reads

## Expected boundaries

- should separate UI rendering from data access
- should avoid broad folder reorganization
- should keep changes inside the feature unless a shared boundary is clearly justified

## Red flags

- cross-feature leakage
- broad folder churn
- new abstraction layers with no local need

## Transcript

`tests/skill-eval/transcripts/codex/montana-frontend-architecture.md`
