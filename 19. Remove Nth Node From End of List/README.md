# Remove Nth Node From End of List

## Problem Description

Given the head of a linked list, remove the nth node from the end of the list and return its head.

### Example

**Input**: `head = [1,2,3,4,5]`, `n = 2`

**Output**: `[1,2,3,5]`

### Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Solution

### Approach

1. **Calculate the Length**:
   - Traverse the list to find its length.
   
2. **Handle Edge Cases**:
   - If the list has only one node, return `None`.
   - If the node to be removed is the first node, update the head to the next node.
   
3. **Find the Node to Remove**:
   - Use a pointer to traverse to the node just before the node to be removed.
   
4. **Remove the Node**:
   - Adjust the `next` pointer to skip the node to be removed.
   
5. **Return the Updated Head**:
   - After making the necessary adjustments, return the updated head of the linked list.

### Time Complexity

The time complexity of this approach is O(sz), where `sz` is the number of nodes in the linked list. This is because we traverse the list twice: once to calculate the length and once to find the node to remove.

### Space Complexity

The space complexity of this approach is O(1) since we only use a few additional variables for counting and traversal.

## Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Helper function to calculate the length of the linked list
        def length(head):
            temp = head
            length = 1
            while temp.next != None:  # Traverse to the end of the list
                temp = temp.next
                length += 1
            return length
        
        # Calculate the length of the linked list
        length = length(head)
        
        # Edge case: if the list has only one node
        if length == 1:
            return None
        
        pointer = head
        
        # Edge case: if the node to be removed is the first node
        if length - n - 1 < 0:
            head = head.next
            return head
        
        # Move the pointer to the (length - n - 1)th node
        for i in range(length - n - 1):
            pointer = pointer.next
        
        # If the node to be removed is not the last node
        if pointer.next.next != None:
            pointer.next = pointer.next.next
        else:
            # If the node to be removed is the last node
            pointer.next = None
        
        return head
```

## Results

- **Runtime**: 7 ms, faster than 98.49% of Python submissions.
- **Memory Usage**: 11.51 MB, less than 70.10% of Python submissions.

## Illustration Table

| Step | Pointer Position | Nodes       | Action                             |
|------|------------------|-------------|------------------------------------|
| 1    | -                | [1,2,3,4,5] | Calculate length: length = 5       |
| 2    | -                | [1,2,3,4,5] | Check edge cases                   |
| 3    | -                | [1,2,3,4,5] | Move pointer to position 3         |
| 4    | Pointer at node 3| [1,2,3,4,5] | Pointer points to node 4           |
| 5    | Pointer at node 3| [1,2,3,5]   | Skip node 4                        |
| 6    | -                | [1,2,3,5]   | Return updated head                |

This approach ensures that we correctly remove the nth node from the end of the list while handling various edge cases.

---
