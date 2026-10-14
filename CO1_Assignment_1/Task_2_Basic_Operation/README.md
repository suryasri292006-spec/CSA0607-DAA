# Task 2 — Basic Operation

The main basic operation is a **key comparison** between a stored registration number and the target.

- Linear search: one equality comparison per visited record.
- Binary search: compare the midpoint value for equality and, if unequal, compare it with the target to choose a half. The code counts these comparisons explicitly.
- Timing is measured with `perf_counter()` and averaged over five executions in the supplied experiment. Timing is machine- and load-dependent; comparisons are more reproducible.
- For successful-search benchmark rows, the target is the middle element by index. This makes the experiment reproducible but is not a full average-case workload.
