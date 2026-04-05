---
name: montana-go-http-boundaries
description: Go decision-spec skill for keeping HTTP handlers thin, mapping transport concerns at the edge, and preserving clean handler-service boundaries.
metadata: {"montana":{"category":"decision","composesWith":["montana-global-contract","montana-go","montana-go-service-patterns","montana-backend-architecture","montana-usecase-delivery","montana-intake"]}}
---

Use this skill when Go work touches HTTP handlers, request parsing, response shaping, status mapping, or transport-specific validation.

## Category
- Decision

## Works with
- `montana-global-contract`
- `montana-go`
- `montana-go-service-patterns`
- `montana-backend-architecture`
- `montana-usecase-delivery`
- `montana-intake`

## Consistency contract (non-negotiables)
- Keep HTTP-specific concerns at the transport edge.
- Keep service/use-case logic independent from `http.Request`, `http.ResponseWriter`, and status-code decisions.
- Make handler flow look similar across endpoints so agents converge on the same structure.

## Montana preferred choices
- Prefer parsing, validation, and transport error mapping in the handler layer.
- Prefer passing domain-safe inputs into services instead of raw request objects.
- Prefer mapping domain/service errors into HTTP responses at the handler boundary.
- Prefer explicit request/response DTOs when the transport shape differs from the domain model.
- Prefer small handlers that orchestrate edge behavior and delegate core work.

## Avoid / anti-patterns
- Passing `*http.Request` into service methods.
- Returning raw HTTP status concerns from domain logic.
- Mixing response writing with business decisions deep in the call stack.
- Embedding persistence or orchestration logic directly in handlers.

## Decision table
- When the handler receives query/body/path data, parse and validate it there.
- When the service needs business inputs, pass clean domain-level parameters or DTOs.
- When a service returns domain errors, map them to status codes/messages in the handler.
- When request and domain shapes differ, create explicit transport types instead of reusing domain structs blindly.

## Default workflow
1. Identify the current HTTP boundary leak, if any.
2. Move request parsing and transport mapping to the handler.
3. Pass clean inputs to the service/use-case layer.
4. Map service results and errors back into HTTP responses.
5. Verify the narrowest handler/service tests possible.

## Output format
- HTTP boundary issue
- Handler/service split chosen
- Commands run
- Contract notes

## Safety rules
- Ask before changing public routes, request schemas, or response contracts.
- Ask before introducing a new router or handler framework pattern.
- Stop and report when the repo intentionally centralizes transport mapping differently.
