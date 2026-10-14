# Task 8 — Implementation and Testing

Source: `Source_Code/search_benchmark.py`

Run from a terminal with Python 3 installed:

```bash
python search_benchmark.py
```

The program:
1. Generates sorted integer registration-number datasets.
2. Runs linear, iterative binary, and recursive binary search.
3. records the found index, key-comparison count, and average elapsed time over five repeats.
4. Writes `benchmark_results.csv`.

### Test cases to execute and capture
| Test | Input | Expected result |
|---|---|---|
| T1 | target is first element | found at index 0 |
| T2 | target is middle element | found at middle index |
| T3 | target is last element | found at final index |
| T4 | target absent but within ID range | `-1` |
| T5 | empty list | `-1` for all three implementations |

The benchmark focuses on successful middle-target searches to provide a consistent comparison. Run additional tests above for correctness evidence.
