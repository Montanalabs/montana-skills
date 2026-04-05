# Codex Transcript: `montana-py`

## Outcome

Pass with executable fallback.

## What Codex did

- inspected `pyproject.toml` to discover project shape
- confirmed the whitespace-normalization failure with a lightweight Python assertion
- noted that `pytest` is not installed in this environment

## Commands attempted

- `python3 -m pytest -q`
- `python3 -c "from src.customer_service import normalize_customer_name; assert normalize_customer_name('  Ada   Lovelace  ') == 'Ada Lovelace'"`

## Assessment

The Python skill is accurate for this kind of bugfix. The fallback verification behavior is especially important here because the configured test runner was unavailable.
