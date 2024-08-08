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
