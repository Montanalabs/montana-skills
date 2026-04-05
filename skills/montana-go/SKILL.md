---
name: montana-go
description: Go workflow helper: gofmt/go test, modules, debugging, and safe refactors.
metadata: {"montana":{"category":"language","composesWith":["montana-global-contract","montana-backend-architecture","montana-usecase-delivery","montana-intake","montana-go-service-patterns","montana-go-http-boundaries","montana-go-testing-patterns","montana-pattern-regression-bugfix"]}}
---

Use this skill when working on Go services/tools, fixing build/test failures, or doing safe refactors.

## Category
- Language

## Works with
- `montana-global-contract`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-intake`
- `montana-go-service-patterns`
- `montana-go-http-boundaries`
- `montana-go-testing-patterns`
- `montana-pattern-regression-bugfix`

## Consistency contract (non-negotiables)
- Follow existing repo conventions/config first (lint rules, error style, folder structure).
- Always run format + tests after changes (or report exactly what prevents that).
- Keep diffs minimal and scoped to the request.
- Exported API changes require explicit confirmation.

## Default workflow
1. Identify module/workspace:
   - Find `go.mod` (and `go.work` if used).
2. Reproduce with the smallest command:
   - `go test ./...` or a focused package test.
3. Make the smallest change that fixes the issue.
4. Format:
   - `gofmt -w <files>` (or rely on editor integration if standard in repo).
5. Re-test:
   - start focused, then widen to `./...` when confident.

## Commands (common)
- Run all tests: `go test ./...`
- Run one package: `go test ./path/to/pkg`
- Run one test: `go test ./path/to/pkg -run TestName`
- Format: `gofmt -w .`
- Modules (only if requested / needed): `go mod tidy`

## Montana Go standards (portable defaults)
Apply these when the repo doesn’t already specify otherwise:
- **Formatting**: always use `gofmt` (never hand-format).
- **Docs**: comment exported identifiers (`// Foo ...`) and packages when needed.
- **Context**: `context.Context` as first arg for request-scoped work; avoid storing contexts in structs.
- **Errors**: wrap errors with context; keep error strings lowercase, no trailing punctuation.
- **Testing**: prefer table-driven tests where appropriate; cover bugfixes with a regression test.
Comment template: `{baseDir}/templates/exported-comment.md`.
Additional templates:
- Package docs: `{baseDir}/templates/package-doc.md`
- Context rules: `{baseDir}/templates/context-guidelines.md`
- Table tests: `{baseDir}/templates/table-driven-test.md`

## Output format
- **What changed**: files touched
- **Commands run**: and results
- **Why it works**: short explanation
- **Next steps**: optional follow-ups

## Safety rules
- Don’t change module dependencies unless asked (avoid surprise `go mod tidy` churn).
- Ask before repo-wide formatting.
- Never request secrets or paste private values into prompts/logs.
- If formatting/tests fail, stop and report the smallest actionable log excerpt plus the next fix to try.
