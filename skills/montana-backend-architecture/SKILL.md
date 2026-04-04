---
name: montana-backend-architecture
description: Backend architecture skill for service boundaries, use-case flow, persistence isolation, and maintainable APIs.
metadata: {"montana":{"category":"architecture","composesWith":["montana-go","montana-py","montana-ts","montana-rust","montana-usecase-delivery"]}}
---

Use this skill when building or modifying backend services, APIs, jobs, or service-layer logic.

## Category
- Architecture

## Works with
- `montana-go`
- `montana-py`
- `montana-ts`
- `montana-rust`
- `montana-usecase-delivery`

## Consistency contract (non-negotiables)
- Keep transport, use-case, domain, and persistence concerns separated.
- Avoid leaking database or framework details through domain/use-case layers.
- Prefer explicit interfaces at boundaries that are likely to change.
- Keep handlers/controllers thin.

## Montana defaults
Apply these when the repo does not already specify otherwise:
- Use request handlers/controllers only for transport mapping and validation.
- Put business rules in use-case or service modules.
- Keep repositories/adapters responsible for persistence and external integration details.
- Make errors meaningful at the boundary the caller sees.

## Default workflow
1. Identify the entrypoint: route, handler, consumer, or job.
2. Trace the use-case flow through service/domain/persistence layers.
3. Apply the smallest change in the correct layer.
4. Verify API contract, error handling, and test impact.
5. Report architectural implications.

## Output format
- What changed
- Boundary/layer impacted
- Commands run
- API or data-flow notes

## Safety rules
- Ask before changing public contracts, schemas, or persistence models.
- Ask before introducing a new framework, ORM pattern, or background processing model.
- Stop and report when the simplest fix would violate the existing architecture.

## Templates
- Use `{baseDir}/templates/service-template.md`
- Use `{baseDir}/templates/repository-boundary.md`
- Use `{baseDir}/templates/request-flow.md`
