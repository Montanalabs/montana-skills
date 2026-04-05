# Case: `montana-ts-runtime-validation`

## Skill under test

`montana-ts-runtime-validation`

## Fixture

`tests/skill-eval/fixtures/ts-react-app`

## Prompt

Harden the cart API boundary so external data is normalized or validated before trusted UI state is set.

## Scoring rubric

- `boundary validation placement`: 4 points
- `runtime/type alignment`: 3 points
- `minimal validation scope`: 2 points
- `clear safety notes`: 1 point

## Expected commands

- read API client and cart files
- typecheck command discovery

## Expected boundaries

- validate or normalize at the edge
- avoid raw casts from external data
- keep downstream UI simpler after boundary validation

## Red flags

- `as` casting raw external data to trusted shape
- validation spread across many consumers
- no runtime fallback for nullable or malformed data

## Transcript

`tests/skill-eval/transcripts/codex/montana-ts-runtime-validation.md`
