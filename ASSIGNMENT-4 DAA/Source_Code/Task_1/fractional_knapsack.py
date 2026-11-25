"""Task 1 - Repaired LoadVehicle (Fractional Knapsack, greedy by value/weight ratio)."""

def load_vehicle(packages, capacity, trace=True):
    """packages: list of (id, weight, value). Returns (fractions dict, total_value)."""
    if capacity < 0:
        raise ValueError("capacity must be >= 0")
    for pid, w, v in packages:
        if w <= 0 or v < 0:
            raise ValueError(f"invalid package {pid}: weight must be > 0, value >= 0")

    # Greedy-choice rule: highest value-per-unit-weight first
    order = sorted(packages, key=lambda p: p[2] / p[1], reverse=True)
    fraction = {p[0]: 0.0 for p in packages}
    remaining, total = capacity, 0.0
    if trace:
        print("Sorted by ratio:", [(p[0], round(p[2] / p[1], 3)) for p in order])
    for pid, w, v in order:
        if remaining == 0:
            break
        if w <= remaining:                       # whole package fits
            fraction[pid] = 1.0
            remaining -= w
            total += v
            action = "take whole"
        else:                                    # partial package, vehicle becomes full
            fraction[pid] = remaining / w
            total += fraction[pid] * v
            action = f"take fraction {remaining}/{w}"
            remaining = 0
        if trace:
            print(f"  {pid}: {action:<22} remaining={remaining:<5} total={total:.2f}")
    return fraction, total


if __name__ == "__main__":
    tests = {
        "T1 classic (cap 50)": ([("P1", 10, 60), ("P2", 20, 100), ("P3", 30, 120)], 50),
        "T2 everything fits (cap 100)": ([("P1", 10, 60), ("P2", 20, 100)], 100),
        "T3 zero capacity": ([("P1", 10, 60)], 0),
        "T4 equal ratios": ([("A", 4, 8), ("B", 2, 4), ("C", 6, 12)], 7),
    }
    for name, (pk, cap) in tests.items():
        print(f"\n=== {name} ===")
        frac, tot = load_vehicle(pk, cap)
        print("Fractions:", {k: round(v, 3) for k, v in frac.items()})
        print("Total value:", round(tot, 2))
