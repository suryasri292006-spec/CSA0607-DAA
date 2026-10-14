# Task 12 — Day-4 Design Challenge

## Workload
- 1,000,000 student records
- 50,000 searches per hour
- New records added once per day

## Request rate
`50,000 / 3,600 ≈ 13.89 searches/second` on average. Capacity planning should also consider peaks, not just the hourly average.

## Operation estimates
At `n=1,000,000`, `log2(n) ≈ 19.93`. Binary search needs at most about 20 midpoint iterations (depending on interval and counting convention). Linear search may inspect up to 1,000,000 records per request. For 50,000 requests/hour, a theoretical upper bound of linear-search record inspections is 50 billion/hour; binary search is around one million midpoint iterations/hour at about 20 per request.

## Recommendation and defence
For an algorithm-only comparison, iterative binary search is the strongest choice if the IDs remain sorted: logarithmic search time and constant auxiliary space. Daily updates make keeping the data sorted manageable in a batch, but inserting into a contiguous array can still shift many records. For the actual system, use a database unique index on registration number. It supports indexed lookups and routine daily inserts without requiring the application to scan a million rows.

## Caveats
These estimates count algorithmic comparisons, not disk I/O, network latency, database contention, authentication, or application overhead. Validate the real service with load testing at and above 13.89 requests/second, and set a response-time objective before deployment.
