# DAA CO1 Assignment Report
## Student Registration Number Search: Design, Analysis, and Scalability Audit

### 1. Problem Statement
Design, implement, execute, and analyse three approaches to search student registration numbers. Compare theoretical and measured performance and recommend an algorithm for one million records with 50,000 search requests per hour and daily record additions.

### 2. Objective
- Implement linear, iterative binary, and recursive binary search.
- Derive basic-operation counts and time/space complexity.
- Evaluate best, average, and worst cases.
- Formulate and solve relevant recurrences.
- Measure comparisons and execution time across multiple input sizes.
- Defend a recommendation for the specified workload.

### 3. Requirements and Environment
- Python 3.x, standard library only for the search implementation.
- Dataset sizes: 100, 1,000, 10,000, 100,000, 1,000,000.
- Registration numbers represented as unique integers.
- Binary search requires sorted input.
- Timer: Python `perf_counter()`, mean of five runs per algorithm/dataset size.
- Dataset construction excluded from the search timing.

### 4. Algorithm Design
The full pseudocode for all three approaches is documented in `Task_1_Algorithm_Design/README.md`. Linear search checks items sequentially. Binary search inspects the midpoint of a sorted range and discards half of the remaining range; iterative binary search uses a loop and recursive binary search uses function calls.

### 5. Basic Operation and Mathematical Analysis
The basic operation is a key comparison. Linear search has a worst-case comparison count proportional to `n`. Binary search halves the remaining search interval after each midpoint decision, so its worst-case number of iterations grows with `log2(n)`.

| Algorithm | Best time | Average time | Worst time | Auxiliary space |
|---|---:|---:|---:|---:|
| Linear search | Θ(1) | Θ(n) | Θ(n) | Θ(1) |
| Iterative binary search | Θ(1) | Θ(log n) | Θ(log n) | Θ(1) |
| Recursive binary search | Θ(1) | Θ(log n) | Θ(log n) | Θ(log n) call stack |

### 6. Recurrence Formulation and Solution
For recursive binary search, `T(n)=T(n/2)+c`. Expanding gives `T(n)=T(n/2^k)+kc`. Stop when `n/2^k=1`, yielding `k=log2(n)`, so `T(n)=T(1)+c log2(n)=Θ(log n)`.
For recursive linear search, `L(n)=L(n-1)+c`; expansion yields `L(n)=L(n-k)+kc`. With `k=n-1`, `L(n)=Θ(n)`.

### 7. Experimental Method
The benchmark searches for the element at index `n//2` in a sorted list. Each search is repeated five times and elapsed time is averaged. The comparison counter is recorded. Because the target is always a successful middle-index target, results are a controlled workload, not a complete distribution-based average-case study. The code and CSV are included in the repository.

### 8. Experimental Results
Measured on the environment where this package was generated. Times are machine-specific and should be re-run on the student's computer before submission.

|   dataset_size | algorithm               | target_type              |   found_index |   comparisons |   average_time_seconds | theoretical_worst_case   |
|---------------:|:------------------------|:-------------------------|--------------:|--------------:|-----------------------:|:-------------------------|
|            100 | Linear Search           | successful_middle_target |            50 |            51 |             2.45e-06   | O(n)                     |
|            100 | Iterative Binary Search | successful_middle_target |            50 |            11 |             1.57e-06   | O(log n)                 |
|            100 | Recursive Binary Search | successful_middle_target |            50 |            11 |             1.74e-06   | O(log n)                 |
|           1000 | Linear Search           | successful_middle_target |           500 |           501 |             2.533e-05  | O(n)                     |
|           1000 | Iterative Binary Search | successful_middle_target |           500 |            17 |             1.59e-06   | O(log n)                 |
|           1000 | Recursive Binary Search | successful_middle_target |           500 |            17 |             2.05e-06   | O(log n)                 |
|          10000 | Linear Search           | successful_middle_target |          5000 |          5001 |             0.000402   | O(n)                     |
|          10000 | Iterative Binary Search | successful_middle_target |          5000 |            25 |             2.5e-06    | O(log n)                 |
|          10000 | Recursive Binary Search | successful_middle_target |          5000 |            25 |             2.93e-06   | O(log n)                 |
|         100000 | Linear Search           | successful_middle_target |         50000 |         50001 |             0.00467482 | O(n)                     |
|         100000 | Iterative Binary Search | successful_middle_target |         50000 |            31 |             1.021e-05  | O(log n)                 |
|         100000 | Recursive Binary Search | successful_middle_target |         50000 |            31 |             1.748e-05  | O(log n)                 |
|        1000000 | Linear Search           | successful_middle_target |        500000 |        500001 |             0.0341874  | O(n)                     |
|        1000000 | Iterative Binary Search | successful_middle_target |        500000 |            37 |             2.05e-05   | O(log n)                 |
|        1000000 | Recursive Binary Search | successful_middle_target |        500000 |            37 |             1.887e-05  | O(log n)                 |

### 9. Graphs
See:
- `Tables_and_Graphs/execution_time.png`
- `Tables_and_Graphs/comparisons.png`

The expected shape is linear growth in the linear-search comparison count and logarithmic growth for binary-search comparison counts. Execution-time curves can be noisy for very short runs.

### 10. Theory vs Experiment
The measured comparison counts should agree with the growth-rate predictions: linear search scales with the target's position, while binary search needs logarithmically many midpoint decisions. Iterative and recursive binary search share the same asymptotic time complexity. Recursive calls may add overhead and require logarithmic stack space. Runtime measurements vary with CPU, interpreter, background tasks, caching, and timer resolution.

### 11. Day-4 Design Challenge
The target request rate is `50,000 / 3,600 ≈ 13.89 requests/second` on average. At one million records, `log2(1,000,000) ≈ 19.93`, so binary search takes around 20 midpoint iterations in the worst case. A linear scan can inspect up to one million records per unsuccessful search. For the algorithm-only choice, iterative binary search is recommended when records are sorted. For a production database, a unique index on the registration number is more appropriate because it supports efficient indexed lookup and normal daily inserts. Load testing is still required to verify peak traffic and response-time targets.

### 12. Test Cases
| Case | Scenario | Expected |
|---|---|---|
| T1 | First ID present | Index 0 |
| T2 | Middle ID present | Middle index |
| T3 | Last ID present | Last index |
| T4 | ID absent | -1 |
| T5 | Empty array | -1 |

Capture terminal screenshots after running the code on your own machine and save them in `Report/Output_Screenshots/`. Capture source-code screenshots in `Report/Source_Code_Screenshots/`.

### 13. Conclusion
The experiment and theory support binary search for repeated searches on sorted registration numbers. Iterative binary search is preferred among the three implementations because it achieves logarithmic time without recursion-stack growth. At system scale, use a database index and validate throughput with load testing. Experimental evidence should be regenerated on the submission computer and screenshots added before submission.

### 14. Individual Contribution
Customize this section truthfully to describe the student's own algorithm design, implementation, testing, analysis, report writing, and repository maintenance.

### 15. References
1. Course material: Design and Analysis of Algorithms, searching and asymptotic analysis.
2. Python documentation: `time.perf_counter()` for elapsed-time measurement.
3. Use the prescribed assignment handout for exact input sizes and submission rules.
