# Case: `montana-py`

## Skill under test

`montana-py`

## Fixture

`tests/skill-eval/fixtures/python-service`

## Prompt

Fix the normalization bug in the customer service, add a regression test, and run the configured Python checks you can.

## Scoring rubric

- `bugfix quality`: 4 points
- `tooling discovery from pyproject`: 2 points
- `regression coverage`: 2 points
- `clear environment-blocker reporting`: 2 points

## Expected commands

- inspection of `pyproject.toml`, source, and tests
- `python3 -m pytest -q` if available
- lightweight fallback command when `pytest` is missing

## Expected boundaries

- should keep the fix readable and local
- should avoid broad typing churn
- should follow the configured Python project shape

## Red flags

- dependency upgrades
- ignoring `pyproject.toml`
- blanket annotation churn

## Transcript

`tests/skill-eval/transcripts/codex/montana-py.md`
