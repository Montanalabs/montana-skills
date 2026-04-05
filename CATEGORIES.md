# Montana Skill Categories

Montana skills are meant to be **composable**. Users can combine:

- a **global contract skill**
- a **language skill**
- a **platform or framework skill**
- an **architecture skill**
- optional **decision skills**
- optional **pattern skills**
- an optional **workflow or use-case skill**

This lets a developer build an agent stack like:

- `montana-global-contract` + `montana-ts` + `montana-ts-style-decisions` + `montana-react`
- `montana-global-contract` + `montana-go` + `montana-go-service-patterns` + `montana-backend-architecture`
- `montana-global-contract` + `montana-rust` + `montana-rust-error-patterns` + `montana-backend-architecture`

For tooling and automation, the machine-readable equivalent lives in `MANIFEST.json`.

## Category model

### 1. Intake
- Understand the repo before editing.
- Example: `montana-intake`

### 2. Global
- Set Montana-wide operating rules that should apply regardless of language or framework.
- Example: `montana-global-contract`

### 3. Language
- Language syntax, linting, docs, testing, and code-style expectations.
- Examples: `montana-rust`, `montana-go`, `montana-py`, `montana-ts`, `montana-js`

### 4. Framework / Platform
- Framework-specific implementation rules and conventions.
- Example: `montana-react`

### 5. Architecture
- Folder structure, boundaries, layering, state/data flow, API design.
- Examples: `montana-frontend-architecture`, `montana-backend-architecture`

### 6. Decision
- Resolve "multiple valid options" into Montana-preferred choices.
- Examples: `montana-ts-style-decisions`, `montana-ts-runtime-validation`, `montana-ts-error-patterns`, `montana-react-rendering-patterns`, `montana-react-state-ownership`, `montana-react-form-patterns`, `montana-go-service-patterns`, `montana-go-http-boundaries`, `montana-go-testing-patterns`, `montana-rust-error-patterns`, `montana-rust-module-boundaries`, `montana-rust-testing-patterns`

### 7. Pattern
- Encode repeatable solution shapes for common implementation problems.
- Examples: `montana-pattern-regression-bugfix`, `montana-pattern-conditional-rendering`

### 8. Use-case / Workflow
- Task-oriented behaviors that cut across languages/frameworks.
- Examples: `montana-usecase-delivery`, `montana-release`

## Composition rules

- A language skill should never try to own frontend/backend architecture by itself.
- A global skill should define default Montana operating rules, not language syntax.
- A framework skill should not redefine basic language rules unless necessary.
- An architecture skill should define boundaries and shape, not language syntax.
- A decision skill should resolve recurring implementation choices that would otherwise drift between agents.
- A pattern skill should define reusable solution shapes, with examples and anti-examples.
- A use-case skill should define delivery expectations, checklists, and outcomes.

## Default recommended stacks

### Frontend React app
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

### Backend API in Go
- `montana-global-contract`
- `montana-intake`
- `montana-go`
- `montana-go-service-patterns`
- `montana-go-http-boundaries`
- `montana-go-testing-patterns`
- `montana-backend-architecture`
- optional: `montana-pattern-regression-bugfix`
- optional: `montana-usecase-delivery`

### Backend service in TypeScript
- `montana-global-contract`
- `montana-intake`
- `montana-ts`
- `montana-ts-style-decisions`
- `montana-ts-runtime-validation`
- `montana-ts-error-patterns`
- `montana-backend-architecture`
- optional: `montana-pattern-regression-bugfix`
- optional: `montana-usecase-delivery`

### Python service
- `montana-global-contract`
- `montana-intake`
- `montana-py`
- `montana-backend-architecture`
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
