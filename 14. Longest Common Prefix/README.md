# Longest Common Prefix

#### Problem Statement
The "Longest Common Prefix" problem (LeetCode #14) requires finding the longest prefix string that is a prefix of all strings in a given array. The problem tests the ability to efficiently traverse and compare strings to find common sequences.

#### Solution Overview
The solution iteratively compares characters of all strings in the list to find the common prefix. It begins with the assumption that the entire first string is the common prefix and reduces it progressively based on mismatches found with subsequent strings.

#### Detailed Explanation
- **Initialization**: The longest common prefix (`lcp`) is initially set to the first string in the array.
- **Comparison**: The solution iterates over each string in the list and compares it with the current `lcp`. If a discrepancy is found, the `lcp` is reduced.
- **Result**: The `lcp` is updated only when a shorter matching sequence is found, ensuring that it always represents the longest common prefix for all strings processed so far.

#### Step-by-Step Solution Example
Consider the array of strings `["flower","flow","flight"]`. Here's how the solution finds the longest common prefix step-by-step:

| Step | Current LCP | Word Compared | Action | New LCP |
|------|-------------|---------------|--------|---------|
| 1    | flower      | flow          | Compare and find common prefix | flow   |
| 2    | flow        | flight        | Compare and find common prefix | fl     |

#### Illustration Table
Here is a breakdown of how the common prefix is determined through iteration:

| Comparison | flower vs. flow | Result |
|------------|-----------------|--------|
| f vs. f    | Match           | f      |
| l vs. l    | Match           | fl     |
| o vs. o    | Match           | flo    |
| w vs. w    | Match           | flow   |
| e vs.       | Mismatch        | flow truncated to 'flow' |

| Comparison | flow vs. flight | Result |
|------------|-----------------|--------|
| f vs. f    | Match           | f      |
| l vs. l    | Match           | fl     |
| o vs. i    | Mismatch        | 'fl' is the longest common prefix |


#### Complexity Analysis
- **Time Complexity**: \(O(S)\), where \(S\) is the sum of all characters in all strings. In the worst case, all comparisons might happen.
- **Space Complexity**: \(O(1)\). Only constant space is used beyond the input strings.

#### Performance Metrics
- **Runtime**: 10 ms, faster than 94.23% of Python submissions.
- **Memory Usage**: 11.96 MB, less efficient than 19.97% of submissions.

#### Conclusion
This solution demonstrates an efficient approach to determining the longest common prefix using a character-by-character comparison and immediate truncation of the prefix upon finding a mismatch. It ensures that the algorithm remains efficient even as the number of strings or the length of the strings increases.

---
