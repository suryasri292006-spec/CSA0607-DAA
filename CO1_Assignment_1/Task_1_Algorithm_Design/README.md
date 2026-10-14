# Task 1 — Algorithm Design

## Problem
Given a collection of student registration numbers and a target registration number, return the target's index if found, or `-1` otherwise.

### Approach 1: Linear Search
Check each element from left to right until the target is found or the list ends.

```text
LINEAR-SEARCH(A, target)
  for i = 0 to length(A)-1
    if A[i] == target
      return i
  return -1
```

### Approach 2: Iterative Binary Search
Precondition: `A` is sorted in ascending order. Keep low/high bounds and repeatedly inspect the midpoint.

```text
ITERATIVE-BINARY-SEARCH(A, target)
  low = 0; high = length(A)-1
  while low <= high
    mid = low + floor((high-low)/2)
    if A[mid] == target: return mid
    else if A[mid] < target: low = mid+1
    else: high = mid-1
  return -1
```

### Approach 3: Recursive Binary Search
Use the same midpoint decision, but solve the remaining half through a recursive call.

```text
RECURSIVE-BINARY-SEARCH(A, target, low, high)
  if low > high: return -1
  mid = low + floor((high-low)/2)
  if A[mid] == target: return mid
  if A[mid] < target:
    return RECURSIVE-BINARY-SEARCH(A, target, mid+1, high)
  return RECURSIVE-BINARY-SEARCH(A, target, low, mid-1)
```

The two binary-search approaches require sorted data; linear search does not. The supplied program uses integer IDs and Python's standard library only.
