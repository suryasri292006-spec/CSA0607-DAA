# Task 7 — Recurrence Solution

## Recursive binary search (expansion)
`T(n)=T(n/2)+c`
`=T(n/4)+2c`
`=T(n/8)+3c`
After `k` expansions: `T(n)=T(n/2^k)+kc`.

Stop when `n/2^k=1`, so `k=log2(n)`. Therefore:
`T(n)=T(1)+c log2(n)=Θ(log n)`.

## Recursive linear search (expansion)
`L(n)=L(n-1)+c`
`=L(n-2)+2c`
`=L(n-k)+kc`.
Stop at `n-k=1`, hence `k=n-1`; therefore `L(n)=d+c(n-1)=Θ(n)`.

The iterative binary search has the same time complexity as recursive binary search but avoids recursive call-stack overhead.
