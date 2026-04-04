# Runtime validation template (montana-ts)

Use runtime validation at boundaries (HTTP, env vars, user input) when the app needs safety beyond TS types.

```ts
export function parseId(input: unknown): string {
  if (typeof input !== "string" || input.length === 0) {
    throw new Error("invalid id");
  }
  return input;
}
```

