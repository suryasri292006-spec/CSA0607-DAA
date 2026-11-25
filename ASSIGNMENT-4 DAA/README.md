# CO4 – Assignment 4A: Algorithmic Design Through Pseudocode

**Course Outcome:** CO4 – Solve optimization problems using Dynamic Programming and Greedy strategies
**Student:** _<name>_  |  **Register No.:** _<register number>_

This repository contains the solutions to all six tasks of Assignment 4A, including the compulsory Day-4 Design Challenge (Task 6).
Each algorithm was designed as pseudocode, traced by hand, challenged with a counter-example, and only then implemented in Python to verify it.

## Repository structure

```
CO4_Assignment_4A/
├── Source_Code/
│   ├── Task_1/  fractional_knapsack.py   (+ output.txt, output_screenshot.png)
│   ├── Task_2/  job_sequencing.py
│   ├── Task_3/  knapsack_01.py
│   ├── Task_4/  word_break.py
│   ├── Task_5/  shortest_paths.py
│   └── Task_6/  weighted_interval.py
├── Report/
│   └── CO4_Assignment_4A_Report.pdf      (analysis, pseudocode, traces, tests, code, output)
└── README.md
```

## How to run

Requires Python 3.8+ (standard library only).

```bash
cd Source_Code/Task_1 && python3 fractional_knapsack.py
cd ../Task_2 && python3 job_sequencing.py
cd ../Task_3 && python3 knapsack_01.py
cd ../Task_4 && python3 word_break.py
cd ../Task_5 && python3 shortest_paths.py
cd ../Task_6 && python3 weighted_interval.py
```

## Summary of tasks and results

| Task | Problem | Strategy | Result |
|------|---------|----------|--------|
| 1 | Repair `LoadVehicle` (divisible packages) | Greedy by value/weight ratio, fraction for the last package | Sample (cap 50): 240 |
| 2 | Job sequencing with deadlines | Greedy: highest profit first, latest free slot ≤ deadline | Schedule C, A, D – profit **180**; with B = 90 → B, A, D = **210** |
| 3 | 0/1 knapsack, capacity 7 | DP `DP[i][w]` with include/exclude and reconstruction | Items **Q, R**, value **45** |
| 4 | Word-break defect | Missing `DP[j] = TRUE` in the test; fixed minimally | `abc` / `{bc}`: wrong TRUE → correct FALSE |
| 5 | Shortest paths on the given graph | Dijkstra, Bellman-Ford (negative edges / cycle), Floyd–Warshall | Dist from A: B4 C6 D7 E10 |
| 6 | Energy-aware job scheduling | DP over jobs sorted by finish time (weighted interval scheduling) | Jobs **J2, J5, J7, J8**, value **200** |

Task 6 was validated against brute force on the given data, on a student-designed adversarial dataset (DP = 180 while earliest-finish, highest-value and shortest-duration greedy give 155 / 145 / 155) and on 500 random instances (0 mismatches).

## Notes

- Pseudocode follows the ALGORITHM / INPUT / OUTPUT / BEGIN / END style of the assignment sheet; programs are only used to verify the designs.
- `substring(Text, j, i)` in Task 4 means characters `j … i-1` of a 0-indexed string.
- Tie rule in Task 6: when Include = Exclude the job is excluded; this does not change the optimal value.
