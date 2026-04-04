# Project conventions discovery checklist

Use this to extract and apply repo-specific rules so all agent work stays consistent.

## Where to look
- `README.md`, `CONTRIBUTING.md`, `docs/`
- Tooling configs: `.editorconfig`, `eslint*`, `prettier*`, `tsconfig*`, `pyproject.toml`, `Cargo.toml`, `clippy.toml`, `golangci*`
- CI: `.github/workflows/*`, `Makefile`, `Taskfile.yml`, `justfile`

## What to capture
- Formatting tools and exact commands
- Lint rules and required flags
- Test commands and expected speed (unit vs integration)
- Naming conventions and file layout
- API and module boundary rules
- Doc requirements (rustdoc/go docstrings/JSDoc)

## How to apply
- Prefer repo rules over Montana defaults.
- If repo rules are missing/unclear, fall back to Montana defaults and state that you did.

