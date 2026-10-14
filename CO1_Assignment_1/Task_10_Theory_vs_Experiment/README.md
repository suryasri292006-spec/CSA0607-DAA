# Task 10 — Theory vs Experiment

Theory predicts linear growth for linear search and logarithmic growth for both binary-search variants. The experimental comparison counts should reflect this: linear search visits about half the array for a middle-index target, while binary search needs only a small number of midpoint checks.

Measured time is affected by interpreter overhead, CPU speed, operating-system scheduling, caching, and timer resolution. Recursive binary search may be slightly slower than iterative binary search because of function-call overhead, even though both have `Θ(log n)` time. Do not infer asymptotic complexity from a single timing point; compare multiple sizes and operation counts.
