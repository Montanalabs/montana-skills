# Frontend state ownership checklist

- Is this state local UI state, shared app state, or server state?
- Can this value be derived instead of stored?
- Is the owner component/module the narrowest valid owner?
- Are loading, empty, success, and error states explicit?

