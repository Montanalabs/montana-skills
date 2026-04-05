export type CartSummary = {
  itemCount: number;
  totalLabel: string | null;
};

export async function fetchCartSummary(): Promise<CartSummary> {
  return {
    itemCount: 2,
    totalLabel: null,
  };
}
