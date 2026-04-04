# Definition of Done (Montana)

Use this as the default completion checklist for agent work.

## Required before “done”
- Reproduction is documented (what command fails / what user sees).
- Smallest fix applied (no unrelated refactors).
- Formatting run (repo-configured).
- Lint/typecheck run (repo-configured).
- Tests run (at least scoped tests; widen if risk is higher).
- Public-facing docs updated if behavior/API changed.
- A regression test is added for bugfixes (when feasible).

## Output requirements (what the agent must report)
- Files changed (list)
- Commands run (exact commands) + short results
- Any skipped checks + why
- Risks / follow-ups

## “Stop and ask” situations
- Large renames/mass formatting
- Dependency/toolchain upgrades
- Public API changes
- Security-sensitive changes (auth, crypto, secrets handling)

