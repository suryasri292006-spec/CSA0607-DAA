"""Task 3 - 0/1 Knapsack by dynamic programming with solution reconstruction."""

def knapsack(items, W, trace=True):
    """items: list of (id, weight, value). DP[i][w] = best value using first i items, capacity w."""
    n = len(items)
    DP = [[0] * (W + 1) for _ in range(n + 1)]          # base: DP[0][*] = 0
    for i in range(1, n + 1):                           # row i-1 is complete before row i
        _, wt, val = items[i - 1]
        for w in range(0, W + 1):
            DP[i][w] = DP[i - 1][w]                     # exclude
            if wt <= w:                                 # include only if feasible
                DP[i][w] = max(DP[i][w], val + DP[i - 1][w - wt])
    chosen, w = [], W                                   # reconstruction by backtracking
    for i in range(n, 0, -1):
        if DP[i][w] != DP[i - 1][w]:                    # value changed => item i was taken
            chosen.append(items[i - 1][0])
            w -= items[i - 1][1]
    chosen.reverse()
    if trace:
        print("DP table (rows = items considered, cols = capacity 0..%d)" % W)
        print("      " + " ".join(f"{c:>3}" for c in range(W + 1)))
        for i in range(n + 1):
            label = "none" if i == 0 else items[i - 1][0]
            print(f"{label:>5} " + " ".join(f"{DP[i][c]:>3}" for c in range(W + 1)))
    return DP[n][W], chosen, DP


if __name__ == "__main__":
    items = [("P", 2, 12), ("Q", 3, 20), ("R", 4, 25), ("S", 5, 30)]
    best, chosen, DP = knapsack(items, 7)
    print("\nOptimum value:", best, " Items chosen:", chosen)
    print("Total weight of chosen items:", sum(w for i, w, v in items if i in chosen))

    from itertools import combinations
    bf = max(sum(v for _, _, v in c) for r in range(len(items) + 1)
             for c in combinations(items, r) if sum(w for _, w, _ in c) <= 7)
    print("Brute-force optimum:", bf, "-> match" if bf == best else "-> MISMATCH")

    print("\n--- Edge cases ---")
    print("Capacity 0:", knapsack(items, 0, trace=False)[:2])
    print("Capacity 1 (nothing fits):", knapsack(items, 1, trace=False)[:2])
    print("Capacity 14 (all fit):", knapsack(items, 14, trace=False)[:2])
