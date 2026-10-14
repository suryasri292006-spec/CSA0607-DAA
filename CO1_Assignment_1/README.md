# CO1 Assignment — Student Registration Number Search

## Overview
This project compares Linear Search, Iterative Binary Search, and Recursive Binary Search for student registration numbers. It includes algorithm design, complexity analysis, recurrence derivation, benchmark code, measured CSV results, graphs, and the Day-4 design challenge.

## Requirements
- Python 3.x
- No third-party packages are required to run the search benchmark.
- Graphs and the included report were generated using pandas/matplotlib in the preparation environment. They do not need those packages to run the benchmark itself.

## Run
```bash
cd Task_8_Implementation_Testing/Source_Code
python search_benchmark.py
```
The program prints the measured index, comparisons, and average elapsed time, then creates `benchmark_results.csv` beside the script.

## Algorithms
1. Linear Search — works with unsorted or sorted data; worst-case Θ(n).
2. Iterative Binary Search — requires sorted data; worst-case Θ(log n), Θ(1) auxiliary space.
3. Recursive Binary Search — requires sorted data; worst-case Θ(log n), Θ(log n) call-stack space.

## Repository Structure
- `Task_1_Algorithm_Design/` — algorithm descriptions and pseudocode.
- `Task_2_Basic_Operation/` — basic operation identification.
- `Task_3_Mathematical_Complexity/` — derivations.
- `Task_4_Case_Analysis/` — best/average/worst-case analysis.
- `Task_5_Asymptotic_Analysis/` — asymptotic notation.
- `Task_6_Recurrence_Formulation/` — recurrence equations.
- `Task_7_Recurrence_Solution/` — step-by-step recurrence solutions.
- `Task_8_Implementation_Testing/` — source code and test instructions.
- `Task_9_Experimental_Performance/` — measured CSV data.
- `Task_10_Theory_vs_Experiment/` — interpretation.
- `Task_11_Final_Recommendation/` — algorithm recommendation.
- `Task_12_Design_Challenge/` — one-million-record/50,000-searches-per-hour challenge.
- `Report/` — final report, evidence folders, graphs, and tables.

## Important submission checklist
- Re-run the benchmark on your own computer and retain the output.
- Add genuine source-code and terminal screenshots to the designated folders.
- Verify the dataset sizes against the exact faculty handout; the provided sizes are 100, 1,000, 10,000, 100,000, and 1,000,000.
- Personalize the individual-contribution section truthfully.
- Upload the complete folder to your GitHub repository.
