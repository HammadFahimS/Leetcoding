# 4SUM
## Problem Statement

Given an array `nums` of `n` integers and an integer `target`, are there elements `a`, `b`, `c`, and `d` in `nums` such that `a + b + c + d` = `target`? Find all unique quadruplets in the array which gives the sum of `target`.

## Solution Approach

### Algorithm

1. **Sorting the Array**: First, sort the array to facilitate the two-pointer technique and help in avoiding duplicates.
2. **Nested Loops**: Utilize two nested loops to fix the first two numbers. 
3. **Two Pointers**: For each pair fixed by the outer loops, use a two-pointer technique to find pairs that complete the quadruplets which sum to the target.
4. **Avoid Duplicates**: Store the results in a dictionary to automatically handle duplicate quadruplets, ensuring each quadruplet is unique.

### Time Complexity

- **O(n^3)**: The algorithm involves two nested loops, and for each iteration of the inner loop, a two-pointer scan is executed. This results in a cubic time complexity.

### Space Complexity

- **O(m)**: Where `m` is the number of unique quadruplets. The primary space usage is for storing the quadruplets in a dictionary.

## Results

- **Runtime**: 813 ms, beats 29.55% of Python online submissions.
- **Memory Usage**: 11.60 MB, beats 74.74% of Python online submissions.

## Step-by-Step Example (Using an Example Array)

Let's consider an example with `nums = [1, 0, -1, 0, -2, 2]` and `target = 0`:

### Illustration Table

| Step | Fixed Numbers | Remaining Numbers | Two Pointer Result | Quadruplets Found | Sum Calculation |
|------|---------------|-------------------|--------------------|-------------------|-----------------|
| 1    | 1, 0          | -1, 0, -2, 2      | -2, 2              | [1, 0, -2, 2]     | 1 + 0 - 2 + 2 = 1 (skip) |
| 2    | 1, -1         | 0, 0, 2           | 0, 0               | [1, -1, 0, 0]     | 1 - 1 + 0 + 0 = 0 (add) |
| 3    | 0, -1         | 0, -2, 2          | -2, 2              | [0, -1, -2, 2]    | 0 - 1 - 2 + 2 = -1 (skip) |
| ...  | ...           | ...               | ...                | ...               | ...             |
| 4    | 0, 0          | -2, 2             | -2, 2              | [0, 0, -2, 2]     | 0 + 0 - 2 + 2 = 0 (add) |
| 5    | -1, -2        | 0, 2              | 0, 2               | [-1, -2, 0, 2]    | -1 - 2 + 0 + 2 = -1 (skip) |

This example would iterate through all possible combinations, checking sums, and storing unique valid quadruplets.

---
