# Student registration-number search algorithm comparison
# Run: python search_benchmark.py
# Python 3.x; standard library only.
# Registration numbers are unique integers stored in sorted order for binary search.

from time import perf_counter
import csv
import math
from pathlib import Path

def linear_search(data, target):
    comparisons = 0
    for i, value in enumerate(data):
        comparisons += 1
        if value == target:
            return i, comparisons
    return -1, comparisons

def iterative_binary_search(data, target):
    low, high = 0, len(data) - 1
    comparisons = 0
    while low <= high:
        mid = low + (high - low) // 2
        comparisons += 1
        if data[mid] == target:
            return mid, comparisons
        comparisons += 1
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

def recursive_binary_search(data, target):
    def search(low, high, comparisons):
        if low > high:
            return -1, comparisons
        mid = low + (high - low) // 2
        comparisons += 1
        if data[mid] == target:
            return mid, comparisons
        comparisons += 1
        if data[mid] < target:
            return search(mid + 1, high, comparisons)
        return search(low, mid - 1, comparisons)
    return search(0, len(data) - 1, 0)

def measure(fn, data, target, repeats=3):
    # Repeat the operation to reduce timer noise; report average elapsed time.
    total = 0.0
    result = None
    for _ in range(repeats):
        start = perf_counter()
        result = fn(data, target)
        total += perf_counter() - start
    return result[0], result[1], total / repeats

def main():
    sizes = [100, 1000, 10000, 100000, 1000000]
    output = Path(__file__).with_name("benchmark_results.csv")
    rows = []
    for n in sizes:
        data = list(range(100000000, 100000000 + n))
        # Middle target gives a reproducible successful-search comparison.
        target = data[n // 2]
        for name, fn in [
            ("Linear Search", linear_search),
            ("Iterative Binary Search", iterative_binary_search),
            ("Recursive Binary Search", recursive_binary_search),
        ]:
            index, comparisons, seconds = measure(fn, data, target)
            rows.append({
                "dataset_size": n,
                "algorithm": name,
                "target_type": "successful_middle_target",
                "found_index": index,
                "comparisons": comparisons,
                "average_time_seconds": f"{seconds:.10f}",
                "theoretical_worst_case": (
                    "O(n)" if name == "Linear Search" else "O(log n)"
                ),
            })
            print(f"n={n:>7} | {name:<24} | index={index:>7} | "
                  f"comparisons={comparisons:>7} | avg_seconds={seconds:.10f}")
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nResults saved to: {output}")

if __name__ == "__main__":
    main()
