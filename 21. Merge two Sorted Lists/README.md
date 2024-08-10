# Merge Two Sorted Lists

## Problem Description

You are given two sorted linked lists, `list1` and `list2`. The goal is to merge these two linked lists into a single sorted linked list. The merged linked list should be created by splicing together the nodes of the first two lists.

### Example

```python
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Constraints

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## Solution

The problem can be solved using an iterative approach where we traverse both lists simultaneously, comparing their current nodes and adding the smaller one to the merged list.

### Step-by-Step Approach

1. **Initialization**: 
    - Create a new linked list called `merged`.
    - Initialize pointers for both `list1` and `list2`.

2. **Iterate Through Both Lists**:
    - Compare the current node of `list1` and `list2`.
    - Append the smaller node to the `merged` list.
    - Move the pointer of the list from which the node was added.

3. **Handle Remaining Nodes**:
    - If one of the lists is exhausted, append the remaining nodes of the other list directly to the `merged` list.

4. **Return the Head of the Merged List**.

### Time Complexity

- **Time Complexity**: O(n + m), where `n` is the number of nodes in `list1` and `m` is the number of nodes in `list2`. This is because we are traversing both lists once.
- **Space Complexity**: O(1), since we're not using any additional data structures and we're modifying the input lists in place.

## Results

- **Runtime**: 10 ms, faster than 98.18% of Python submissions.
- **Memory Usage**: 11.64 MB, better than 53.50% of Python submissions.

## Step-by-Step Illustration

| Step | list1 Pointer | list2 Pointer | Merged List  |
|------|---------------|---------------|--------------|
| 1    | 1             | 1             | 1            |
| 2    | 2             | 1             | 1 -> 1       |
| 3    | 2             | 3             | 1 -> 1 -> 2  |
| 4    | 4             | 3             | 1 -> 1 -> 2 -> 3  |
| 5    | 4             | 4             | 1 -> 1 -> 2 -> 3 -> 4 |
| 6    | -             | 4             | 1 -> 1 -> 2 -> 3 -> 4 -> 4 |

### Explanation:

- At each step, the pointers move through `list1` and `list2`, comparing the values and adding the smaller one to the merged list.
- The process continues until all nodes are added to the `merged` list.

## Conclusion
This solution efficiently merges two sorted linked lists with minimal space complexity. The results are highly optimized, achieving both high runtime performance and reasonable memory usage.

---
