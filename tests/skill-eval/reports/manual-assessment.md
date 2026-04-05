# Manual Assessment

## Overall take

The skills are structurally strong:

- consistent frontmatter
- consistent section layout
- good composability metadata
- concrete safety rules
- referenced templates are present

That means the pack is already in good shape as a reusable instruction library.

## What looks strong

- The language skills are practical and repo-first rather than overly prescriptive.
- The architecture skills keep boundaries clear and do not overstep into language-specific rules.
- `montana-intake` and `montana-usecase-delivery` are good stack-level glue skills.
- `montana-release` is appropriately confirmation-first.

## What lowers confidence today

- Static consistency is excellent, but live model behavior still depends on how well the runtime applies multiple skills together.
- The checked-in transcripts currently cover Codex only. Claude and OpenClaw still need the same saved-run treatment if they become target runtimes.
- The case files are now scored rubrics, but they are still reviewer-scored rather than fully auto-graded.

## Accuracy verdict

- Instruction accuracy inside the skill files: high
- Repo/documentation accuracy: high
- End-to-end runtime proof in this repo: medium to high for Codex, medium overall across runtimes

## Suggested next improvements

- Add Claude and OpenClaw transcript sets if those runtimes become release targets.
- Consider a small auto-grading layer for command expectations and transcript freshness.
- Decide whether the older `tmp/skill-eval` scratch area should be removed now that `tests/skill-eval` is the permanent home.
