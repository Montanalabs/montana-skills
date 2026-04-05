# Case: `montana-rust-testing-patterns`

## Skill under test

`montana-rust-testing-patterns`

## Fixture

`tests/skill-eval/fixtures/rust-cli`

## Prompt

Use the smallest Rust test strategy that proves zero is an invalid port, add or refine the regression case if needed, and widen verification only after the focused case is clear.

## Scoring rubric

- `focused test strategy`: 4 points
- `regression coverage`: 2 points
- `clear boundary of behavior under test`: 2 points
- `sensible widening`: 2 points

## Expected commands

- `cargo test`
- focused read of crate source and tests

## Expected boundaries

- narrow regression-oriented test first
- explicit contract under test
- broader verification only after local confidence

## Red flags

- vague “does not panic” style testing
- no regression case
- broad testing without a local reproduction story

## Transcript

`tests/skill-eval/transcripts/codex/montana-rust-testing-patterns.md`
