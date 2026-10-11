# CSA06 - Design and Analysis of Algorithms
# CO1 - Assessment Tool 1
# Project: ShopSphere Scalability Audit
#
# Server Processing Rate: 10^8 operations per second
# Maximum Processing Time: 600 seconds (10 minutes)

import math

SERVER_RATE = 10**8
TIME_LIMIT = 600


# M1: Pairwise Duplicate Comparisons
# Time Complexity: Theta(n^2)
# Space Complexity: Theta(1)

def m1_pairwise_comparisons(n):
    return n * (n - 1) // 2


# M2: Hierarchical Audit
# Operation count: 2^ceil(log2(n)) - 1
# Time Complexity: Theta(n)

def m2_hierarchical_audit(n):
    if n <= 1:
        return 0

    level = math.ceil(math.log2(n))
    return (2 ** level) - 1


# S2: Repeated Halving
# Recurrence: T(n) = T(n/2) + 1
# Time Complexity: Theta(log n)

def s2_repeated_halving(n):
    if n <= 1:
        return 1

    return math.ceil(math.log2(n)) + 1


# M4: Current Divide-and-Conquer Algorithm
# Recurrence: T(n) = 4T(n/2) + n
# Time Complexity: Theta(n^2)

def m4_current(n):
    level = math.ceil(math.log2(n))
    padded_n = 2 ** level

    return 2 * padded_n**2 - padded_n


# M4: Proposed Improved Algorithm
# Recurrence: T(n) = 2T(n/2) + n
# Time Complexity: Theta(n log n)

def m4_improved(n):
    level = math.ceil(math.log2(n))
    padded_n = 2 ** level

    return padded_n * (level + 1)


# M5: Divide-and-Conquer Algorithm
# Recurrence: T(n) = 2T(n/2) + n log2(n)
# Time Complexity: Theta(n log^2(n))

def m5_algorithm(n):
    if n <= 1:
        return 1

    level = math.ceil(math.log2(n))
    padded_n = 2 ** level

    return padded_n * (level * (level + 1) // 2 + 1)


# Combined operation-count function
# f(n) = 3n^2 + 10n log2(n) + 50
# Time Complexity: Theta(n^2)

def combined_function(n):
    return math.ceil(
        3 * n**2 + 10 * n * math.log2(n) + 50
    )


# Convert operation count into execution time

def execution_time(operations):
    return operations / SERVER_RATE


# Display analysis for each input size

def analyze(n):
    algorithms = {
        "M1 - Pairwise Comparisons":
            m1_pairwise_comparisons(n),

        "M2 - Hierarchical Audit":
            m2_hierarchical_audit(n),

        "S2 - Repeated Halving":
            s2_repeated_halving(n),

        "M4 - Current Algorithm":
            m4_current(n),

        "M4 - Improved Algorithm":
            m4_improved(n),

        "M5 - Divide and Conquer":
            m5_algorithm(n),

        "Combined Function f(n)":
            combined_function(n)
    }

    print("\n" + "=" * 75)
    print(f"SHOPSHPERE SCALABILITY AUDIT: n = {n:,}")
    print("=" * 75)

    print(f"{'Algorithm':<32}{'Operations':>22}"
          f"{'Time (seconds)':>20}")

    print("-" * 75)

    for name, operations in algorithms.items():
        seconds = execution_time(operations)

        print(
            f"{name:<32}"
            f"{operations:>22,.0f}"
            f"{seconds:>20,.6f}"
        )

    print("-" * 75)
    print(f"Server processing rate: {SERVER_RATE:,} operations/sec")
    print(f"Time limit: {TIME_LIMIT} seconds (10 minutes)")

    combined_ops = combined_function(n)
    total_time = execution_time(combined_ops)

    if total_time <= TIME_LIMIT:
        print("Combined function: WITHIN the 10-minute limit.")
    else:
        print("Combined function: EXCEEDS the 10-minute limit.")

    print("=" * 75)


# Main program

if __name__ == "__main__":

    print("DAA - CO1 ASSESSMENT TOOL 1")
    print("ShopSphere Scalability Audit")

    analyze(100_000)
    analyze(1_000_000)
