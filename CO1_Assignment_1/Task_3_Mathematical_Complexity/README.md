# Task 3 — Mathematical Complexity

Let `n` be the number of registration numbers.

## Linear search
For a successful target at position `i`, the algorithm performs `i+1` equality tests. For a miss it performs `n` equality tests. Thus the worst-case count is `C(n)=n`, giving `T(n)=a n+b` and `Θ(n)`.

## Binary search
Each iteration removes approximately half of the remaining candidates. If `C(n)` is the number of midpoint iterations, then `C(n) ≤ floor(log2(n))+1` for non-empty arrays. Hence `T(n)=a log2(n)+b` and `Θ(log n)`.

## Space
- Linear search: `Θ(1)` auxiliary space.
- Iterative binary search: `Θ(1)` auxiliary space.
- Recursive binary search: `Θ(log n)` call-stack space in the worst case, due to recursive depth.
