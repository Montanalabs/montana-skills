# Montana Skills Pack v0.1.0

Initial public release of the Montana Skills Pack: a composable open-source skills package for engineering agents.

## Highlights

- Introduces a category-based skills system instead of a flat list
- Ships self-contained skills for language, framework, architecture, intake, release, and use-case delivery workflows
- Adds authoring templates so new skills can be created and updated consistently
- Includes machine-readable package metadata and a formal support matrix
- Includes release scripts and runtime adapter starter kits

## Included skills

### Intake
- `montana-intake`

### Languages
- `montana-rust`
- `montana-go`
- `montana-py`
- `montana-ts`
- `montana-js`

### Frameworks
- `montana-react`

### Architecture
- `montana-frontend-architecture`
- `montana-backend-architecture`

### Use-case / Workflow
- `montana-usecase-delivery`
- `montana-release`

## What’s included in the release artifact

- canonical `skills/` source pack
- `templates/` for authoring and maintenance
- `MANIFEST.json` for machine-readable category and composition metadata
- `SUPPORT_MATRIX.md` for runtime support stance
- `adapters/` starter kits for Claude, Codex, and OpenClaw
- `scripts/` for package validation and release building

## Support status

- OpenClaw: supported directly from the canonical skill folders
- Claude Code: adapter kit included
- Codex: adapter kit included

## Notes

- The canonical source is runtime-neutral.
- Runtime-specific packaging should be built from the canonical pack and adapter kits.
- Consistency across teams still depends on repo-level tooling and CI enforcement.

