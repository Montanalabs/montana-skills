# Case: `montana-react-rendering-patterns`

## Skill under test

`montana-react-rendering-patterns`

## Fixture

`tests/skill-eval/fixtures/ts-react-app`

## Prompt

Rework a cart summary component so it renders async states in Montana order and avoids nested JSX branching.

## Scoring rubric

- `state ordering`: 4 points
- `early-return branch clarity`: 3 points
- `accessible state feedback`: 2 points
- `minimal branch churn`: 1 point

## Expected commands

- read cart component files
- identify async state sources

## Expected boundaries

- prefer loading -> error -> empty -> content
- prefer early returns over nested ternaries
- keep branches explicit and readable

## Red flags

- nested ternary rendering
- silent `null` return for meaningful states
- duplicated UI state just for rendering

## Transcript

`tests/skill-eval/transcripts/codex/montana-react-rendering-patterns.md`
