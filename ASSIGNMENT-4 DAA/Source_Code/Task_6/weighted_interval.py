"""Task 6 - Energy-aware job scheduling = Weighted Interval Scheduling (dynamic programming)."""
import random
from itertools import combinations

def schedule(jobs, trace=True):
    """jobs: list of (id, start, finish, value). Returns (max_value, selected ids)."""
    J = sorted(jobs, key=lambda j: j[2])                 # preprocessing: sort by finish time
    n = len(J)
    # p[j] = largest index k < j with finish_k <= start_j (touching allowed), else 0  (1-indexed)
    p = [0] * (n + 1)
    for j in range(1, n + 1):
        lo, hi, best = 1, j - 1, 0                       # binary search for rightmost compatible job
        while lo <= hi:
            mid = (lo + hi) // 2
            if J[mid - 1][2] <= J[j - 1][1]:
                best = mid; lo = mid + 1
            else:
                hi = mid - 1
        p[j] = best
    OPT = [0] * (n + 1)                                  # OPT[0] = 0 (no jobs)
    take = [False] * (n + 1)
    for j in range(1, n + 1):
        incl = J[j - 1][3] + OPT[p[j]]
        excl = OPT[j - 1]
        if incl > excl:
            OPT[j], take[j] = incl, True
        else:
            OPT[j] = excl
        if trace:
            print(f"  j={j} {J[j-1][0]}: p={p[j]}  include={J[j-1][3]}+OPT[{p[j]}]={incl:<4} exclude=OPT[{j-1}]={excl:<4} -> OPT[{j}]={OPT[j]} ({'INCLUDE' if take[j] else 'exclude'})")
    sel, j = [], n                                       # reconstruction
    while j > 0:
        if take[j]:
            sel.append(J[j - 1][0]); j = p[j]
        else:
            j -= 1
    sel.reverse()
    return OPT[n], sel

def brute(jobs):
    best = (0, [])
    for r in range(len(jobs) + 1):
        for c in combinations(jobs, r):
            ok = all(a[2] <= b[1] or b[2] <= a[1] for a, b in combinations(c, 2))
            v = sum(j[3] for j in c)
            if ok and v > best[0]: best = (v, [j[0] for j in c])
    return best

# --- greedy heuristics (used ONLY to show why they are rejected) ---
def greedy(jobs, key):
    chosen, last_end, tot = [], -1e9, 0
    for j in sorted(jobs, key=key):
        if all(j[2] <= c[1] or c[2] <= j[1] for c in chosen):
            chosen.append(j); tot += j[3]
    return tot, [c[0] for c in chosen]

GREEDIES = {"earliest finish": lambda j: j[2], "highest value": lambda j: -j[3],
            "shortest duration": lambda j: j[2] - j[1]}

if __name__ == "__main__":
    jobs = [("J1",1,3,20),("J2",2,5,50),("J3",4,6,30),("J4",6,8,40),
            ("J5",5,9,60),("J6",8,10,30),("J7",9,11,50),("J8",11,13,40)]
    print("=== Given 8-job dataset ===")
    v, s = schedule(jobs)
    print("Selected:", s, " Total energy-saving value:", v)
    print("Brute force:", brute(jobs)[0])
    for name, k in GREEDIES.items(): print(f"  greedy({name}) -> {greedy(jobs, k)}")

    adv = [("K1",4,6,50),("K2",10,11,50),("K3",6,8,55),("K4",3,6,40),("K5",4,10,95),("K6",2,6,75)]
    print("\n=== Adversarial dataset (6 jobs) ===")
    for j in adv: print("  ", j)
    for name, k in GREEDIES.items(): print(f"  greedy({name}) -> {greedy(adv, k)}")
    print("DP trace:")
    v, s = schedule(adv)
    print("DP selected:", s, " value:", v, " | brute force:", brute(adv))

    print("\n=== Randomised verification vs brute force (500 tests) ===")
    random.seed(7); bad = 0
    for _ in range(500):
        n = random.randint(1, 9)
        T = [(f"R{i}", (s0 := random.randint(0, 12)), s0 + random.randint(1, 6), random.randint(1, 50)) for i in range(n)]
        if schedule(T, trace=False)[0] != brute(T)[0]: bad += 1
    print("Mismatches:", bad)
