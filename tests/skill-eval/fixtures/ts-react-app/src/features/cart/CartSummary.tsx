import { useEffect, useState } from "react";
import { fetchCartSummary } from "./api";

export function CartSummary() {
  const [totalLabel, setTotalLabel] = useState("");

  useEffect(() => {
    fetchCartSummary().then((summary) => {
      setTotalLabel(summary.totalLabel.toUpperCase());
    });
  }, []);

  return <p>Total: {totalLabel}</p>;
}
