# Release checklist template (confirmation-first)

## Pre-flight (must be green)
- [ ] Pull latest main/default branch
- [ ] Run format/lint/typecheck (repo scripts)
- [ ] Run tests (repo scripts)
- [ ] Build artifacts (repo scripts)

## Versioning
- [ ] Bump version in the canonical file(s)
- [ ] Update changelog

## Tagging & publishing (ask before running)
- [ ] Create tag `vX.Y.Z`
- [ ] Push tag
- [ ] Create GitHub Release with notes
- [ ] Publish to ecosystem registry (if any)

## Post-release
- [ ] Verify install/upgrade path
- [ ] Announce release (optional)

