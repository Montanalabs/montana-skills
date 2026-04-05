# Case: `montana-rust-error-patterns`

## Skill under test

`montana-rust-error-patterns`

## Fixture

`tests/skill-eval/fixtures/rust-cli`

## Prompt

Fix the invalid-port behavior so zero is rejected with explicit error handling and no convenience unwraps or public API expansion.

## Scoring rubric

- `explicit error flow`: 4 points
- `no unsafe shortcuts`: 2 points
- `public surface preserved`: 2 points
- `focused verification`: 2 points

## Expected commands

- read `Cargo.toml` and `src/lib.rs`
- `cargo test`

## Expected boundaries

- no `unwrap()` or `expect()` in production path
- preserve current function signature
- keep errors meaningful

## Red flags

- changing return type without need
- `unwrap()` in fix path
- leaking internal details in public error surface

## Transcript

`tests/skill-eval/transcripts/codex/montana-rust-error-patterns.md`
