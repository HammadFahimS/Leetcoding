# 3Sum Solution

#### Problem Statement
The "3Sum" problem (LeetCode #15) requires finding all unique triplets in an array that sum up to zero. The challenge is to do this efficiently, avoiding brute force methods that result in a high time complexity.

#### Solution Overview
This solution employs a combination of sorting the array and using the two-pointer technique to find triplets that sum to zero, which improves efficiency compared to the naive approach.

#### Detailed Explanation
1. **Sort the Array**: Start by sorting the array. This helps in efficiently finding the triplets and managing duplicates.
2. **Two-Pointer Technique**: For each element in the array, use two pointers to find pairs that with the current element sum to zero.

#### Step-by-Step Process
Here's a step-by-step breakdown using an example array `[-1, 0, 1, 2, -1, -4]` sorted to `[-4, -1, -1, 0, 1, 2]`:

| Step | Fixed Element | Left Pointer | Right Pointer | Sum   | Action              |
|------|---------------|--------------|---------------|-------|---------------------|
| 1    | -4            | -1           | 2             | -3    | Increase left pointer  |
| 2    | -1            | -1           | 2             | 0     | Found triplet, move pointers |
| 3    | -1            | 0            | 1             | 0     | Found triplet, move pointers |
| 4    | 0             | 1            | 2             | 3     | Decrease right pointer |


#### Complexity Analysis
- **Time Complexity**: The overall complexity is \(O(n^2)\). Sorting the array takes \(O(n \log n)\), and the two-pointer search takes \(O(n)\) for each element.
- **Space Complexity**: \(O(1)\) for the space required by the two-pointer technique. Note: This does not include the space required to store the output.

#### Performance Metrics
- **Runtime**: 5978 ms, this solution is slower and only beats 6.52% of Python submissions.
- **Memory Usage**: 15.19 MB, more efficient in terms of memory usage, beating 39.70% of submissions.

#### Conclusion
While this solution effectively identifies all unique triplets that sum to zero, its performance could be optimized. Considerations for optimization might include more efficient management of duplicates and exploring other data structures or algorithms to reduce the number of necessary comparisons.

---
