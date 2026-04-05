---
name: montana-go-service-patterns
description: Go decision-spec skill for service-layer boundaries, interface placement, constructor patterns, and handler/service separation.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-go","montana-backend-architecture","montana-usecase-delivery","montana-intake"]}}
---

Use this skill when working on Go services, handlers, or business-layer logic where multiple clean designs are possible.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-go`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-intake`

## Consistency contract (non-negotiables)
- Keep transport concerns out of service logic.
- Keep persistence details behind interfaces or adapters when the boundary is likely to change.
- Make Go service code read similarly across repos by using the same responsibility split.

## Montana preferred choices
- Prefer consumer-owned interfaces rather than defining interfaces next to implementations by default.
- Prefer constructor functions when a type has dependencies, invariants, or non-trivial setup.
- Prefer services/use-cases for business rules and orchestration.
- Prefer handlers/controllers for request parsing, validation, transport mapping, and response shaping only.
- Prefer explicit dependency fields over package-level globals.

## Avoid / anti-patterns
- Business logic in handlers.
- Defining interfaces "just in case" when there is no consumer boundary.
- Package-level mutable state for service dependencies.
- Returning transport-specific errors directly from domain/service logic without mapping.

## Default workflow
1. Identify the boundary: handler, service, repository, or adapter.
2. Move validation and transport-specific work to the edge when possible.
3. Keep business rules and orchestration in the service layer.
4. Place interfaces with the consumer that needs abstraction.
5. Verify tests at the narrowest affected package.

## Decision table
- When a handler receives input, keep parsing and validation there.
- When business rules depend on multiple dependencies or branches, prefer a service/use-case layer.
- When only one concrete dependency exists and no consumer boundary needs abstraction, avoid introducing an interface.
- When a consumer needs to mock or swap behavior, define the interface near that consumer.

## Output format
- Boundary affected
- Pattern chosen
- Commands run
- Data-flow notes

## Safety rules
- Ask before changing public handler contracts or request/response schemas.
- Ask before broad package reorganizations.
- Stop if the repo already has a conflicting service pattern and report the tradeoff.
