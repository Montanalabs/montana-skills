# Rust error handling guidelines (Montana defaults)

## Defaults
- Avoid `unwrap()`/`expect()` in non-test code paths.
- Prefer returning `Result<T, E>` from fallible operations.
- Add context to errors where it helps debugging (follow repo patterns; `anyhow`, `thiserror`, custom enums).

## When `unwrap()` is acceptable
- Tests
- Prototypes (only with explicit user approval)
- Invariants proven by construction (rare; document the invariant)

