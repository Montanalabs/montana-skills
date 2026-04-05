# Case: `montana-global-contract`

## Skill under test

`montana-global-contract`

## Fixture

`tests/skill-eval/fixtures/python-service`

## Prompt

Fix the customer-name normalization bug with the smallest safe change, verify it with the narrowest useful command, and report blockers clearly if the full test toolchain is unavailable.

## Scoring rubric

- `repo-first workflow`: 3 points
- `minimal diff discipline`: 3 points
- `narrow verification behavior`: 2 points
- `stable reporting shape`: 2 points

## Expected commands

- read `pyproject.toml`, source, and tests
- `python3 -m pytest -q` if available
- narrow fallback command if `pytest` is missing

## Expected boundaries

- should not bundle unrelated cleanup
- should verify narrowly before widening
- should report what changed, what ran, and what remains blocked

## Red flags

- broad refactor during a local bugfix
- silent blocker handling
- repo-agnostic guesses instead of reading fixture files

## Transcript

`tests/skill-eval/transcripts/codex/montana-global-contract.md`
