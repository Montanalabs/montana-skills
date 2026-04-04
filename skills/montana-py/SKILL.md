---
name: montana-py
description: Python workflow helper: venv/deps, ruff/black, mypy, pytest, and safe refactors.
metadata: {"montana":{"category":"language","composesWith":["montana-backend-architecture","montana-usecase-delivery","montana-intake"]}}
---

Use this skill when working on Python apps/libraries, fixing failing tests, improving typing, or refactoring safely.

## Category
- Language

## Works with
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-intake`

## Consistency contract (non-negotiables)
- Follow repo conventions/configs first (`pyproject.toml`, lint/format settings, test runner).
- Always format/lint/typecheck/test if the repo supports it (or report exactly what blocks you).
- Keep diffs minimal, reviewable, and scoped to the request.
- Behavior changes require updating docs/tests and calling it out explicitly.

## Default workflow
1. Identify the Python project shape:
   - `pyproject.toml` vs `requirements.txt` vs `setup.cfg`
   - src layout (`src/`), package name, test runner
2. Identify the environment/deps approach used by the repo:
   - venv + pip, uv, poetry, pip-tools, conda (follow repo docs)
3. Reproduce:
   - run the smallest `pytest` (or equivalent) command to reproduce failures
4. Apply the smallest change
5. Run format/lint/typecheck (only those configured in the repo)
6. Re-run tests

## Commands (pick what the repo uses)
- Create venv (example): `python -m venv .venv`
- Activate (bash/zsh): `source .venv/bin/activate`
- Lint/format (ruff): `ruff check .` and `ruff format .`
- Format (black): `black .`
- Typecheck (mypy): `mypy .`
- Tests: `pytest -q` (or `pytest path/to/test.py::test_name`)

## Montana Python standards (portable defaults)
Apply these when the repo doesn’t already specify otherwise:
- **Docstrings**: use Google-style docstrings for exported/public functions/classes.
- **Typing**: add type hints for public functions and non-trivial internal functions; avoid `Any` unless justified.
- **Errors**: raise specific exceptions; include actionable messages; don’t swallow exceptions silently.
- **Style**: prefer explicit code over clever one-liners; keep functions small.
- **Testing**: add a regression test for bugfixes; keep tests deterministic (no network/time dependencies unless mocked).
Docstring template: `{baseDir}/templates/google-docstring.md`.
Additional templates:
- pytest tests: `{baseDir}/templates/pytest-test.md`
- Error style: `{baseDir}/templates/error-style.md`
- Type hints: `{baseDir}/templates/type-hinting.md`

## Refactor rules (safe defaults)
- Keep diffs small; avoid drive-by changes.
- Prefer explicit, readable code over clever one-liners.
- Add/adjust types gradually; don’t blanket-annotate everything unless asked.
- Update tests when behavior changes, and explain behavior changes clearly.

## Output format
- **What changed**: files touched
- **Commands run**: and results
- **Why**: 1–3 bullets tied to the failure/feature
- **Next steps**: optional follow-ups

## Safety rules
- Never ask for or print secrets (tokens, API keys, passwords).
- Avoid dependency upgrades unless explicitly requested.
- Ask before reformatting the whole repo.
- If lint/format/typecheck/tests fail, stop and report the smallest actionable log excerpt plus the next fix to try.
