# React component template (montana-react)

```tsx
type ExampleProps = {
  title: string;
  onSelect?: () => void;
};

/**
 * Renders an example UI block.
 */
export function Example({ title, onSelect }: ExampleProps) {
  return (
    <section>
      <h2>{title}</h2>
      <button type="button" onClick={onSelect}>
        Select
      </button>
    </section>
  );
}
```

