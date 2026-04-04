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

- install **one skill** by copying one folder from `package/skills/`
- install **a stack** by copying the recommended folders for that stack
- install **the whole pack** by copying everything under `package/skills/`

Fastest examples:

**Install one skill**

```bash
mkdir -p skills
cp -R package/skills/montana-release skills/
```

**Install a React frontend stack**

```bash
mkdir -p skills
cp -R package/skills/montana-intake skills/
cp -R package/skills/montana-ts skills/
cp -R package/skills/montana-react skills/
cp -R package/skills/montana-frontend-architecture skills/
```

**Install the whole pack**

```bash
mkdir -p skills
cp -R package/skills/* skills/
```

For Claude Code and Codex, use the adapter kits in `package/adapters/`.

## What’s inside

Skills live in `package/skills/`:

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

### Use-case / Workflow
- `montana-usecase-delivery` — request scoping, acceptance criteria, definition of done
- `montana-release` — changelog/release notes + safe release checklist

See `package/CATEGORIES.md` for the composition model.
See `package/MANIFEST.json` for machine-readable categories, composition, and recommended stacks.

## Recommended stacks

### React frontend app
- `montana-intake`
- `montana-ts`
- `montana-react`
- `montana-frontend-architecture`
- optional: `montana-usecase-delivery`

### Go backend API
- `montana-intake`
- `montana-go`
- `montana-backend-architecture`
- optional: `montana-usecase-delivery`

### TypeScript backend service
- `montana-intake`
- `montana-ts`
- `montana-backend-architecture`
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
- Full pack: every folder under `package/skills/`

## Consistency promise (what this pack can and can’t guarantee)

These skills aim to make agent output **highly consistent** by:
- enforcing the same “read → plan → edit → verify” workflow
- prescribing portable style/doc/testing standards when the repo doesn’t specify them
- requiring format/lint/typecheck/tests to pass (or reporting blockers)

However, **100% consistency across all developers/projects requires tooling + enforcement**:
- formatters/linters/typecheckers configured in the repo
- CI that blocks merges when checks fail

This pack guides agents to use those tools; it cannot replace them.

## Safety guarantees (by design)

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
mkdir -p skills
cp -R package/skills/montana-release skills/
```

#### Install a stack

Example: React frontend stack

```bash
mkdir -p skills
cp -R package/skills/montana-intake skills/
cp -R package/skills/montana-ts skills/
cp -R package/skills/montana-react skills/
cp -R package/skills/montana-frontend-architecture skills/
```

Example: Go backend stack

```bash
mkdir -p skills
cp -R package/skills/montana-intake skills/
cp -R package/skills/montana-go skills/
cp -R package/skills/montana-backend-architecture skills/
```

#### Install the whole pack

```bash
mkdir -p skills
cp -R package/skills/* skills/
```

Then invoke in OpenClaw using the installed skill names. Slash command support depends on your UI/config.

### Claude Code
Claude support is shipped as an **adapter kit**, not as a claimed direct install surface.

If you want Claude support:

1. Choose one skill, a stack, or the whole pack from `package/skills/`.
2. Use `package/adapters/claude/` to map that selection into Claude-specific commands or agents.
3. Verify the generated Claude-facing files against the current Claude runtime surface before distributing them to users.

Included in the adapter kit:

- `package/adapters/claude/README.md`
- `package/adapters/claude/MANIFEST.json`
- `package/adapters/claude/COMMAND_TEMPLATE.md`
- `package/adapters/claude/AGENT_TEMPLATE.md`

### Codex
Codex support is also shipped as an **adapter kit**.

If you want Codex support:

1. Choose one skill, a stack, or the whole pack from `package/skills/`.
2. Use `package/adapters/codex/` to wrap that selection for the Codex surface you support.
3. Verify the generated Codex-facing files against the current Codex runtime surface before distributing them to users.

Included in the adapter kit:

- `package/adapters/codex/README.md`
- `package/adapters/codex/MANIFEST.json`
- `package/adapters/codex/PROMPT_TEMPLATE.md`
- `package/adapters/codex/SKILL_WRAPPER_TEMPLATE.md`

See `package/maintainers/PUBLISHING.md` for the supported distribution stance.
See `package/SUPPORT_MATRIX.md` for the publication support contract.

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
To create or update skills consistently, use:

- `package/templates/SKILL_TEMPLATE.md`
- `package/templates/SKILL_CHECKLIST.md`
- `package/templates/STACK_TEMPLATE.md`
- `package/adapters/`
- `package/MANIFEST.json`
- `package/.gitignore`

## License

See `package/LICENSE`.

## Publishing (maintainers)

If you’re publishing this pack for public users, follow `package/maintainers/PUBLISHING.md`.
