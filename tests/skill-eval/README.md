# Skill Evaluation Workflow

This is the permanent evaluation harness for the Montana skills pack.

It covers four things:

1. static consistency checks for the skill files
2. fixture repos that expose realistic bugs or workflow tasks
3. scored case rubrics for each skill
4. saved runtime transcripts for reproducible review

## Layout

- `scripts/evaluate_skills.py`
- `fixtures/`
- `cases/`
- `transcripts/codex/`
- `reports/`

## Run the evaluator

From the repository root:

```bash
python3 tests/skill-eval/scripts/evaluate_skills.py
```

Generated files:

- `tests/skill-eval/reports/skill-evaluation.json`
- `tests/skill-eval/reports/skill-evaluation.md`

## Transcripts

The checked-in transcripts capture example runtime behavior for the cases currently exercised in this repo.
