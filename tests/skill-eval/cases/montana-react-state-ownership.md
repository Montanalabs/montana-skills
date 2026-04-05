# Case: `montana-react-state-ownership`

## Skill under test

`montana-react-state-ownership`

## Fixture

`tests/skill-eval/fixtures/ts-react-app`

## Prompt

Adjust the checkout flow so state stays in the narrowest correct owner, derived values are not stored redundantly, and hook extraction is avoided unless it clearly improves reuse or clarity.

## Scoring rubric

- `state kept near owner`: 4 points
- `derived state avoided`: 2 points
- `no unnecessary hook extraction`: 2 points
- `clear ownership explanation`: 2 points

## Expected commands

- read checkout component and nearby feature files

## Expected boundaries

- keep state local unless multiple consumers require lifting
- derive display booleans when practical
- avoid abstraction for one-off state logic

## Red flags

- lifting state without need
- storing duplicate derived state
- extracting a hook for one local path

## Transcript

`tests/skill-eval/transcripts/codex/montana-react-state-ownership.md`
