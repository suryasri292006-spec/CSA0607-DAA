# Task 4 — Best, Average, and Worst Cases

| Algorithm | Best case | Average case | Worst case | Reason |
|---|---|---|---|---|
| Linear search | Θ(1) | Θ(n) | Θ(n) | Target may be first, typically requires a linear scan, or may be last/absent |
| Iterative binary search | Θ(1) | Θ(log n) | Θ(log n) | First midpoint may match; otherwise repeatedly halves interval |
| Recursive binary search | Θ(1) | Θ(log n) | Θ(log n) | Same decisions as iterative version, with recursive calls |

Average-case linear search assumes a target is equally likely to occur at any position and is present: expected comparisons are `(n+1)/2`. If unsuccessful searches are also included, the exact average depends on the proportion of successful and unsuccessful requests.

For binary search, successful target positions require logarithmic-scale comparisons on average; worst-case remains logarithmic. Exact counts depend on `n` and target position.
