# Case: `montana-rust-module-boundaries`

## Skill under test

`montana-rust-module-boundaries`

## Fixture

`tests/skill-eval/fixtures/rust-cli`

## Prompt

Keep the Rust CLI fix internal by default, avoid widening visibility without need, and preserve a small intentional public surface.

## Scoring rubric

- `narrow visibility choice`: 4 points
- `public surface discipline`: 3 points
- `module-boundary reasoning`: 2 points
- `minimal API churn`: 1 point

## Expected commands

- read crate root and source file
- `cargo test`

## Expected boundaries

- prefer `pub(crate)` or private where possible
- avoid gratuitous re-exports
- keep module structure responsibility-driven

## Red flags

- widening visibility by default
- public API churn unrelated to the fix
- deep hierarchy with no ownership benefit

## Transcript

`tests/skill-eval/transcripts/codex/montana-rust-module-boundaries.md`
