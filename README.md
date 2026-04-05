<p align="center">
  <img src="assets/logo.png" alt="Montana Skills logo" width="180">
</p>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-v0.1.0-black">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-white">
</p>

<p align="center"><strong>Compatible with OpenClaw, Claude Code, and Codex.</strong></p>

# Montana Skills Pack

Montana Skills Pack is an open-source collection of **self-contained, production-oriented, composable skills** for engineering agents.

Instead of shipping only one skill per language, the pack is designed so users can combine:

- a language skill
- a framework skill
- an architecture skill
- an optional use-case or workflow skill

All skills use a shared **Agent Skills-style** authoring format (`SKILL.md` with YAML frontmatter + Markdown instructions), and the canonical source is kept runtime-neutral.

## Quick start

If you are using OpenClaw:

- install **one skill** by copying one folder from `skills/`
- install **a stack** by copying the recommended folders for that stack
- install **the whole pack** by copying everything under `skills/`

Fastest examples:

If you are already inside the destination workspace, you can avoid typing the full path by targeting the current directory:

```bash
WORKSPACE_DIR="${PWD}"
```

If you are not in the destination workspace yet, replace `WORKSPACE_DIR` with the workspace path you want.

**Install one skill**

```bash
mkdir -p "$WORKSPACE_DIR/skills"
cp -R skills/montana-release "$WORKSPACE_DIR/skills/"
```

**Install a React frontend stack**

```bash
mkdir -p "$WORKSPACE_DIR/skills"
cp -R skills/montana-intake "$WORKSPACE_DIR/skills/"
cp -R skills/montana-ts "$WORKSPACE_DIR/skills/"
cp -R skills/montana-react "$WORKSPACE_DIR/skills/"
cp -R skills/montana-frontend-architecture "$WORKSPACE_DIR/skills/"
```

**Install the whole pack**

```bash
mkdir -p "$WORKSPACE_DIR/skills"
cp -R skills/* "$WORKSPACE_DIR/skills/"
```

For Claude Code and Codex, use the adapter kits in `adapters/`.

## What’s inside

Skills live in `skills/`:

### Intake
- `montana-intake` — project understanding + “how to proceed” checklist

### Languages
- `montana-rust` — cargo workflow, refactors, debugging, testing
- `montana-go` — gofmt/go test, modules, refactors, debugging
- `montana-py` — venv, ruff/black, mypy, pytest, safe refactors
- `montana-ts` — typecheck, lint/format, migrations, safe refactors
- `montana-js` — Node tooling, lint/format/test, safe refactors

### Frameworks
- `montana-react` — React UI implementation, state flow, accessibility

### Architecture
- `montana-frontend-architecture` — feature structure, UI boundaries, state ownership
- `montana-backend-architecture` — handlers/services/repositories, persistence isolation

### Global + Decision
- `montana-global-contract` — Montana-wide operating rules for predictable agent behavior
- `montana-ts-style-decisions` — TypeScript decision rules for functions, type modeling, exports, constants, and nullability
- `montana-ts-runtime-validation` — TypeScript runtime-boundary validation rules for external input
- `montana-ts-error-patterns` — TypeScript failure modeling, propagation, and actionable error rules
- `montana-react-rendering-patterns` — React rendering order and branch-structure rules
- `montana-react-state-ownership` — React state location, derived state, and hook extraction rules
- `montana-react-form-patterns` — React form submit, validation feedback, and accessible error-state rules
- `montana-go-service-patterns` — Go service, handler, and interface-placement rules
- `montana-go-http-boundaries` — Go HTTP handler transport-boundary rules
- `montana-go-testing-patterns` — Go focused-test, table-test, and regression-test rules
- `montana-rust-error-patterns` — Rust error and visibility decision rules
- `montana-rust-module-boundaries` — Rust module visibility and public-surface rules
- `montana-rust-testing-patterns` — Rust focused verification and regression-testing rules

### Patterns
- `montana-pattern-regression-bugfix` — repeatable Montana bugfix flow: reproduce, isolate, fix narrowly, add regression protection, verify
- `montana-pattern-conditional-rendering` — repeatable Montana UI state ordering and early-return rendering pattern

### Use-case / Workflow
- `montana-usecase-delivery` — request scoping, acceptance criteria, definition of done
- `montana-release` — changelog/release notes + safe release checklist

See `CATEGORIES.md` for the composition model.
See `MANIFEST.json` for machine-readable categories, composition, and recommended stacks.

## Recommended stacks

### React frontend app
- `montana-global-contract`
- `montana-intake`
- `montana-ts`
- `montana-ts-style-decisions`
- `montana-ts-runtime-validation`
- `montana-ts-error-patterns`
- `montana-react`
- `montana-react-rendering-patterns`
- `montana-react-state-ownership`
- `montana-react-form-patterns`
- `montana-frontend-architecture`
- optional: `montana-pattern-conditional-rendering`
- optional: `montana-pattern-regression-bugfix`
- optional: `montana-usecase-delivery`

### Go backend API
- `montana-global-contract`
- `montana-intake`
- `montana-go`
- `montana-go-service-patterns`
- `montana-go-http-boundaries`
- `montana-go-testing-patterns`
- `montana-backend-architecture`
- optional: `montana-pattern-regression-bugfix`
- optional: `montana-usecase-delivery`

### TypeScript backend service
- `montana-global-contract`
- `montana-intake`
- `montana-ts`
- `montana-ts-style-decisions`
- `montana-ts-runtime-validation`
- `montana-ts-error-patterns`
- `montana-backend-architecture`
- optional: `montana-pattern-regression-bugfix`
- optional: `montana-usecase-delivery`

### Rust backend service
- `montana-global-contract`
- `montana-intake`
- `montana-rust`
- `montana-rust-error-patterns`
- `montana-rust-module-boundaries`
- `montana-rust-testing-patterns`
- `montana-backend-architecture`
- optional: `montana-pattern-regression-bugfix`
- optional: `montana-usecase-delivery`

## Install options

Choose the smallest install that matches your goal:

- **One skill** if you only need one behavior, such as `montana-release`
- **A recommended stack** if you want a focused setup, such as React frontend or Go backend
- **The whole pack** if you want the full Montana system available

Common examples:

- Single skill: `montana-release`
- Frontend stack: `montana-intake`, `montana-ts`, `montana-react`, `montana-frontend-architecture`
- Backend stack: `montana-intake`, `montana-go`, `montana-backend-architecture`
- Full pack: every folder under `skills/`

## Consistency promise (what this pack can and can’t guarantee)

These skills aim to make agent output **highly consistent** by:
- enforcing the same “read → plan → edit → verify” workflow
- prescribing portable style/doc/testing standards when the repo doesn’t specify them
- requiring format/lint/typecheck/tests to pass (or reporting blockers)

However, **100% consistency across all developers/projects requires tooling + enforcement**:
- formatters/linters/typecheckers configured in the repo
- CI that blocks merges when checks fail

This pack guides agents to use those tools; it cannot replace them.


These skills are written for public use:

- No instructions to exfiltrate secrets or upload `.env`/keys.
- No “curl | sh” patterns in default flows.
- “Read → plan → edit → verify” workflow emphasis.
- Requires confirmation before destructive actions (mass delete, renames across repo, dependency upgrades, release tagging).

## Runtime support

### OpenClaw
OpenClaw is the runtime most directly supported by the canonical `skills/` folders.

#### Install one skill

Copy one skill folder into your workspace `skills/` directory:

```bash
mkdir -p "$WORKSPACE_DIR/skills"
cp -R skills/montana-release "$WORKSPACE_DIR/skills/"
```

#### Install a stack

Example: React frontend stack

```bash
mkdir -p "$WORKSPACE_DIR/skills"
cp -R skills/montana-intake "$WORKSPACE_DIR/skills/"
cp -R skills/montana-ts "$WORKSPACE_DIR/skills/"
cp -R skills/montana-react "$WORKSPACE_DIR/skills/"
cp -R skills/montana-frontend-architecture "$WORKSPACE_DIR/skills/"
```

Example: Go backend stack

```bash
mkdir -p "$WORKSPACE_DIR/skills"
cp -R skills/montana-intake "$WORKSPACE_DIR/skills/"
cp -R skills/montana-go "$WORKSPACE_DIR/skills/"
cp -R skills/montana-backend-architecture "$WORKSPACE_DIR/skills/"
```

#### Install the whole pack

```bash
mkdir -p "$WORKSPACE_DIR/skills"
cp -R skills/* "$WORKSPACE_DIR/skills/"
```

Then invoke in OpenClaw using the installed skill names. Slash command support depends on your UI/config.

### Claude Code
Claude support is shipped as an **adapter kit**, not as a claimed direct install surface.

If you want Claude support:

1. Choose one skill, a stack, or the whole pack from `skills/`.
2. Use `adapters/claude/` to map that selection into Claude-specific commands or agents.
3. Verify the generated Claude-facing files against the current Claude runtime surface before distributing them to users.

Included in the adapter kit:

- `adapters/claude/README.md`
- `adapters/claude/MANIFEST.json`
- `adapters/claude/COMMAND_TEMPLATE.md`
- `adapters/claude/AGENT_TEMPLATE.md`

### Codex
Codex support is also shipped as an **adapter kit**.

If you want Codex support:

1. Choose one skill, a stack, or the whole pack from `skills/`.
2. Use `adapters/codex/` to wrap that selection for the Codex surface you support.
3. Verify the generated Codex-facing files against the current Codex runtime surface before distributing them to users.

Included in the adapter kit:

- `adapters/codex/README.md`
- `adapters/codex/MANIFEST.json`
- `adapters/codex/PROMPT_TEMPLATE.md`
- `adapters/codex/SKILL_WRAPPER_TEMPLATE.md`

See `SUPPORT_MATRIX.md` for the publication support contract.

## CI / Audits

This repo includes GitHub Actions for:

- skill-pack integrity auditing via `tests/skill-eval/scripts/audit_repo.py`
- secret scanning with Gitleaks
- workflow linting with `actionlint`
- supply-chain posture checks with OpenSSF Scorecard

These checks fit a skills/prompt repository better than dependency-focused scanners alone, because most of the risk here is content drift, unsafe guidance, and accidental secret exposure rather than package dependency churn.

## Repo metadata

Suggested GitHub repository description:

`Composable open-source skills pack for engineering agents: languages, frameworks, architecture, and delivery workflows.`

Suggested GitHub topics:

- `ai-agents`
- `agent-skills`
- `prompt-engineering`
- `developer-tools`
- `typescript`
- `golang`
- `python`
- `rust`
- `react`
- `openclaw`

## Development

Each skill is **self-contained**. Any templates/examples needed by a skill are bundled inside that skill’s folder.
Common templates live under each skill’s `templates/` directory (for example JSDoc, docstrings, tests, release notes).
To evaluate and maintain skills consistently, use:

- `tests/skill-eval/README.md`
- `tests/skill-eval/scripts/evaluate_skills.py`
- `tests/skill-eval/cases/`
- `tests/skill-eval/transcripts/codex/`
- `MANIFEST.json`
- `adapters/`

## License

See `LICENSE`.
