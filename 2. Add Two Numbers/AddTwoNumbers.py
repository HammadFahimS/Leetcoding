# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Initialize carry to False, which indicates if there's an extra digit to add from the previous sum.
        carry = False
        # Create a dummy head for the result linked list.
        head = ListNode()
        # Pointer to traverse the result linked list.
        pointer = head
        # Variable to store the current digit sum.
        currentDigit = 0
        # Variables to store values of the current nodes of l1 and l2.
        one = l1.val
        two = l2.val

        # Loop until both linked lists are fully traversed.
        while True:
            # Calculate the sum of the current digits.
            currentDigit = one + two
            # Add 1 to the current digit if there's a carry from the previous addition.
            if carry:
                carry = False
                currentDigit += 1

            # Check if the sum is greater than or equal to 10 to determine if there's a carry for the next digit.
            if currentDigit >= 10:
                carry = True
                # Set the current digit to the units place of the sum.
                pointer.val = currentDigit - 10
            else:
                # Set the current digit if there's no carry.
                pointer.val = currentDigit

            # Check if we've reached the end of both linked lists.
            if l1.next == None and l2.next == None:
                # If there's a carry left, add a new node with value 1.
                if carry:
                    pointer.next = ListNode()
                    pointer = pointer.next
                    pointer.val = 1
                break
            else:
                # Move to the next node in the result linked list.
                pointer.next = ListNode()
                pointer = pointer.next

            # Move to the next node in l1 if it exists, otherwise set one to 0.
            if l1.next != None:
                l1 = l1.next
                one = l1.val
            else:
                one = 0

            # Move to the next node in l2 if it exists, otherwise set two to 0.
            if l2.next != None:
                l2 = l2.next
                two = l2.val
            else:
                two = 0

        # Return the head of the result linked list.
        return head
