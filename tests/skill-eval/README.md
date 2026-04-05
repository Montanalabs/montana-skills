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

## Transcript policy

The checked-in transcripts represent the runtime currently prioritized in this repo: Codex.

Each transcript should record:

- the case prompt
- what repo facts were discovered
- what commands were attempted
- what environment blockers existed
- a short judgment of how well the skill guidance held up
