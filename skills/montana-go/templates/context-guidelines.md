# context.Context guidelines (montana-go)

## Defaults
- `context.Context` is the first parameter for request-scoped operations.
- Don’t store contexts in structs.
- Don’t pass nil contexts; use `context.Background()` or `context.TODO()`.
- Timeouts/cancellation should be owned by the caller boundary (handlers/jobs), not deep helpers.

