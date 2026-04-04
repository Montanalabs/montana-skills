# Rust test patterns (montana-rust)

## Defaults
- Prefer unit tests close to the code (`mod tests`).
- Add regression tests for bugfixes.
- Keep tests deterministic (no network/time unless mocked).

## Useful patterns
- Table-driven tests with structs and `#[test]` loops.
- Snapshot tests only if the repo already uses them.

