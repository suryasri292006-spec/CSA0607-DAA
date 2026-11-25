"""Task 2 - Job Sequencing with Deadlines (greedy: highest profit first, latest free slot)."""

def job_sequencing(jobs, trace=True):
    """jobs: list of (id, deadline, profit)."""
    max_d = min(max(j[1] for j in jobs), len(jobs))
    slot = [None] * (max_d + 1)                  # slot[1..max_d]
    total = 0
    for jid, d, p in sorted(jobs, key=lambda j: j[2], reverse=True):
        s = min(d, max_d)
        while s >= 1 and slot[s] is not None:    # scan backwards for a free slot
            s -= 1
        if s >= 1:
            slot[s] = jid
            total += p
            if trace: print(f"  {jid} (d={d}, p={p}): placed in slot {s}  | slots={slot[1:]} total={total}")
        elif trace:
            print(f"  {jid} (d={d}, p={p}): no free slot <= {d} -> REJECT | slots={slot[1:]} total={total}")
    return slot[1:], total


if __name__ == "__main__":
    base = [("A", 2, 80), ("B", 1, 35), ("C", 2, 60), ("D", 3, 40), ("E", 1, 25)]
    print("=== Given instance ===")
    sched, tot = job_sequencing(base)
    print("Schedule (slot1..):", sched, " Total profit:", tot)

    mod = [("A", 2, 80), ("B", 1, 90), ("C", 2, 60), ("D", 3, 40), ("E", 1, 25)]
    print("\n=== Modified: profit(B) 35 -> 90 ===")
    sched, tot = job_sequencing(mod)
    print("Schedule (slot1..):", sched, " Total profit:", tot)

    # brute-force check on given instance
    from itertools import permutations
    best = 0
    for r in range(len(base) + 1):
        for perm in permutations(base, r):
            if all(perm[i][1] >= i + 1 for i in range(r)):
                best = max(best, sum(j[2] for j in perm))
    print("\nBrute-force optimum (given instance):", best)
