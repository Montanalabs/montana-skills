import { useState } from "react";

export function CheckoutForm() {
  const [email, setEmail] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setSaving(true);
    setError("");

    try {
      if (!email.includes("@")) {
        throw new Error("Email is invalid");
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown error");
    } finally {
      setSaving(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>Email</label>
      <input value={email} onChange={(event) => setEmail(event.target.value)} />
      {error ? <div>{error}</div> : null}
      <button type="submit">Place order</button>
    </form>
  );
}
