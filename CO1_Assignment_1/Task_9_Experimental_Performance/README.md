# Task 9 — Experimental Performance

`benchmark_results.csv` contains the measured results from this environment for dataset sizes 100, 1,000, 10,000, 100,000, and 1,000,000. Each elapsed time is the mean of five runs of the search function; dataset construction is excluded.

The target is the element at index `n//2`. Therefore, this is a successful middle-index workload and should not be represented as a complete average-case benchmark for all target distributions. The comparisons column is deterministic for this workload; elapsed time may differ on another computer.

Graphs are saved in `../Report/Tables_and_Graphs/`.
