---
name: montana-rust
description: Rust workflow helper: cargo build/test, fmt/clippy, debugging, and safe refactors.
metadata: {"montana":{"category":"language","composesWith":["montana-global-contract","montana-backend-architecture","montana-usecase-delivery","montana-intake","montana-rust-error-patterns","montana-rust-module-boundaries","montana-rust-testing-patterns","montana-pattern-regression-bugfix"]}}
---

Use this skill when working on Rust code (crates/workspaces), fixing compile errors, adding features, or refactoring safely.

## Category
- Language

## Works with
- `montana-global-contract`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-intake`
- `montana-rust-error-patterns`
- `montana-rust-module-boundaries`
- `montana-rust-testing-patterns`
- `montana-pattern-regression-bugfix`

## Consistency contract (non-negotiables)
- Prefer the repo’s existing conventions/configs over personal preference.
- Never leave the codebase in a failing state: formatting, lint, and tests must pass (or report exactly what blocks them).
- Changes must be minimal, reviewable, and scoped to the request.
- Public API changes require explicit confirmation.

## Default workflow (safe + repeatable)
1. **Locate the Rust entrypoints**
   - Find the nearest `Cargo.toml` (workspace root vs crate).
2. **Reproduce first**
   - Prefer the smallest command that reproduces the problem (compile error, failing test).
3. **Make the smallest change**
   - Avoid unrelated refactors or dependency upgrades.
4. **Format**
   - `cargo fmt` (or `rustfmt` if repo uses it directly).
5. **Lint (if available/expected)**
   - `cargo clippy` (prefer treating warnings as errors if the repo does).
6. **Test**
   - `cargo test` (limit to the affected crate first, then widen if needed).

## Montana Rust standards (portable defaults)
Apply these when the repo doesn’t already specify otherwise:
- **Docs**: add rustdoc (`///`) for `pub` items; add module docs (`//!`) for major modules.
- **Errors**: avoid `unwrap()`/`expect()` in production paths; prefer explicit error handling and context.
- **Naming**: avoid single-letter names except for tiny scopes (like indices in trivial loops).
- **APIs**: prefer small, composable functions; avoid hidden side effects.
- **Formatting**: never hand-format; rely on `cargo fmt`.
If you need a starting point for docs, use `{baseDir}/templates/rustdoc-public.md`.
Additional templates:
- Error handling: `{baseDir}/templates/error-handling.md`
- Module docs: `{baseDir}/templates/module-doc.md`
- Test patterns: `{baseDir}/templates/test-patterns.md`

## Commands (pick the repo-appropriate subset)
- Format: `cargo fmt`
- Lint: `cargo clippy` (optionally: `cargo clippy -- -D warnings`)
- Test: `cargo test`
- Single package: `cargo test -p <crate>`
- Single test: `cargo test <test_name_substring>`

## Refactor rules (public pack defaults)
- Prefer pure refactors that preserve behavior and keep diffs small.
- Do not change public APIs without explicit user confirmation.
- Avoid cleverness: prefer readable, idiomatic Rust.
- Handle errors explicitly; avoid `unwrap()`/`expect()` in production paths unless justified.
- Update docs/examples when behavior changes.

## Debugging checklist
- If a compile error: include the exact error output and the file/line referenced.
- If a failing test: run it in isolation first, then broaden.
- If async: confirm runtime (Tokio/async-std) and feature flags.

## Output format
- **What changed**: list files touched
- **Why**: 1–3 bullets tied to the error or requirement
- **Commands run**: and short results
- **Next steps**: follow-ups (if any)

## Safety rules
- Never instruct users to paste secrets into logs.
- Do not run `cargo update` / dependency upgrades unless asked.
- Ask before doing mass edits (rename modules, reformat entire repo).
- If `cargo fmt`/`clippy`/`test` fails, stop and report the smallest actionable log excerpt plus the next fix to try.
