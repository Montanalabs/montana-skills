# JavaScript error handling (Montana defaults)

## Defaults
- Don’t swallow errors (`catch (e) {}` is not acceptable).
- Add context to errors when rethrowing:

```js
try {
  await doThing();
} catch (err) {
  throw new Error(`doThing failed: ${err instanceof Error ? err.message : String(err)}`);
}
```

