# React hook template (montana-react)

```tsx
type UseExampleOptions = {
  enabled?: boolean;
};

export function useExample({ enabled = true }: UseExampleOptions) {
  // Keep local state minimal and derive when possible.
  return { enabled };
}
```

