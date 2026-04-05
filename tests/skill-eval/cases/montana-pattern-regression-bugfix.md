# Case: `montana-pattern-regression-bugfix`

## Skill under test

`montana-pattern-regression-bugfix`

## Fixture

`tests/skill-eval/fixtures/go-api`

## Prompt

Follow the Montana regression bugfix pattern end to end: reproduce the failing behavior, fix it narrowly, add or preserve regression protection, and report the exact verification path.

## Scoring rubric

- `reproduce first`: 3 points
- `narrow fix`: 3 points
- `regression coverage mindset`: 2 points
- `verification reporting`: 2 points

## Expected commands

- focused reproduction command
- narrow retest after fix

## Expected boundaries

- no unrelated cleanup
- explicit root-cause framing
- regression protection addressed, or blocker explained

## Red flags

- bugfix without reproduction
- broad refactor bundled with fix
- no verification narrative

## Transcript

`tests/skill-eval/transcripts/codex/montana-pattern-regression-bugfix.md`
