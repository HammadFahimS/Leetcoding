class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Directly return True for single-digit positive numbers and 0
        if 0 <= x < 10:
            return True
        
        # Convert the number to a string to facilitate reversal and comparison
        num = str(x)

        # Initialize pointers for the start and end of the string
        start_ptr = 0
        length = len(num)
        end_ptr = length - 1
        
        # Iterate from start to the middle of the string
        for i in range(length // 2):  # Using integer division to get floor value
            # Compare characters from the start and the end moving towards the center
            if num[start_ptr + i] != num[end_ptr - i]:
                return False  # Return False as soon as a mismatch is found
        # If no mismatches are found, the number is a palindrome
        return True
