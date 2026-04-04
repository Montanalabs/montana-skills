# Montana Skill Categories

Montana skills are meant to be **composable**. Public users should be able to combine:

- a **language skill**
- a **platform or framework skill**
- an **architecture skill**
- an optional **workflow or use-case skill**

This lets a developer create an agent stack like:

- `montana-ts` + `montana-react` + `montana-frontend-architecture`
- `montana-go` + `montana-backend-architecture`
- `montana-ts` + `montana-backend-architecture` + `montana-usecase-delivery`

For tooling and automation, the machine-readable equivalent lives in `package/MANIFEST.json`.

## Category model

### 1. Intake
- Understand the repo before editing.
- Example: `montana-intake`

### 2. Language
- Language syntax, linting, docs, testing, and code-style expectations.
- Examples: `montana-rust`, `montana-go`, `montana-py`, `montana-ts`, `montana-js`

### 3. Framework / Platform
- Framework-specific implementation rules and conventions.
- Example: `montana-react`

### 4. Architecture
- Folder structure, boundaries, layering, state/data flow, API design.
- Examples: `montana-frontend-architecture`, `montana-backend-architecture`

### 5. Use-case / Workflow
- Task-oriented behaviors that cut across languages/frameworks.
- Examples: `montana-usecase-delivery`, `montana-release`

## Composition rules

- A language skill should never try to own frontend/backend architecture by itself.
- A framework skill should not redefine basic language rules unless necessary.
- An architecture skill should define boundaries and shape, not language syntax.
- A use-case skill should define delivery expectations, checklists, and outcomes.

## Default recommended stacks

### Frontend React app
- `montana-intake`
- `montana-ts`
- `montana-react`
- `montana-frontend-architecture`
- optional: `montana-usecase-delivery`

### Backend API in Go
- `montana-intake`
- `montana-go`
- `montana-backend-architecture`
- optional: `montana-usecase-delivery`

### Backend service in TypeScript
- `montana-intake`
- `montana-ts`
- `montana-backend-architecture`
- optional: `montana-usecase-delivery`

### Python service
- `montana-intake`
- `montana-py`
- `montana-backend-architecture`
- optional: `montana-usecase-delivery`
