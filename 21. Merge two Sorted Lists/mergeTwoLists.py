# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Initialize the merged list pointer to None
        merged = None
        # This flag helps to identify the first node in the merged list
        first_node = True
        # Pointer to the last node in the merged list
        merged_ptr = None
        # Pointers to traverse list1 and list2
        list1_ptr = list1
        list2_ptr = list2

        # Continue merging while either list1_ptr or list2_ptr is not None
        while list1_ptr != None or list2_ptr != None:
            # If list1 is exhausted, add nodes from list2
            if list1_ptr == None and list2_ptr != None:
                if first_node:
                    # Create the first node in the merged list
                    merged = ListNode(list2_ptr.val)
                    merged_ptr = merged
                    merged.next = None
                    first_node = False
                    list2_ptr = list2_ptr.next
                else:
                    # Add the current list2 node to the merged list
                    merged_ptr.next = ListNode(list2_ptr.val)
                    merged_ptr = merged_ptr.next
                    list2_ptr = list2_ptr.next
            # If list2 is exhausted, add nodes from list1
            elif list1_ptr != None and list2_ptr == None:
                if first_node:
                    # Create the first node in the merged list
                    merged = ListNode(list1_ptr.val)
                    merged_ptr = merged
                    merged.next = None
                    first_node = False
                    list1_ptr = list1_ptr.next
                else:
                    # Add the current list1 node to the merged list
                    merged_ptr.next = ListNode(list1_ptr.val)
                    merged_ptr = merged_ptr.next
                    list1_ptr = list1_ptr.next
            # If neither list1 nor list2 is exhausted, compare their current nodes
            else:
                if list1_ptr.val < list2_ptr.val:
                    if first_node:
                        # Create the first node in the merged list
                        merged = ListNode(list1_ptr.val)
                        merged_ptr = merged
                        merged.next = None
                        first_node = False
                        list1_ptr = list1_ptr.next
                    else:
                        # Add the current list1 node to the merged list
                        merged_ptr.next = ListNode(list1_ptr.val)
                        merged_ptr = merged_ptr.next
                        list1_ptr = list1_ptr.next
                else:
                    if first_node:
                        # Create the first node in the merged list
                        merged = ListNode(list2_ptr.val)
                        merged_ptr = merged
                        merged.next = None
                        first_node = False
                        list2_ptr = list2_ptr.next
                    else:
                        # Add the current list2 node to the merged list
                        merged_ptr.next = ListNode(list2_ptr.val)
                        merged_ptr = merged_ptr.next
                        list2_ptr = list2_ptr.next

        # Return the head of the merged linked list
        return merged
