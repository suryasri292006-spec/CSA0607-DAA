# Task 6 — Recurrence Formulation

For recursive binary search, each call performs constant work and continues on at most half the remaining array:

`T(n) = T(n/2) + c` for `n > 1`, with `T(1)=d`.

For linear search expressed recursively, one possible recurrence is `L(n)=L(n-1)+c`, with `L(1)=d`, because each call checks one item and then may search the remaining `n-1` items. This recursive linear variant is for mathematical analysis; the implementation uses iterative linear search to avoid unnecessary recursion depth.
