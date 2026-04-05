# Case: `montana-rust`

## Skill under test

`montana-rust`

## Fixture

`tests/skill-eval/fixtures/rust-cli`

## Prompt

Fix the parsing bug in the config loader without changing the public API, then run formatting and the smallest relevant test.

## Scoring rubric

- `bugfix correctness`: 4 points
- `public-api preservation`: 2 points
- `cargo fmt and focused test usage`: 2 points
- `explicit error-handling discipline`: 2 points

## Expected commands

- inspection of `Cargo.toml` and `src/lib.rs`
- `cargo test`
- `cargo fmt`

## Expected boundaries

- should reject invalid port zero without changing the return type
- should avoid broad refactors
- should keep explicit error behavior

## Red flags

- public API drift
- `unwrap()` in production flow
- broad refactors

## Transcript

`tests/skill-eval/transcripts/codex/montana-rust.md`
