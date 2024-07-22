class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Helper function to check if all characters in the substring are unique
        def isUnique(s):
            chars = []  # List to store unique characters encountered
            for c in s:  # Iterate over each character in the substring
                if c in chars:
                    return False  # If character is already in list, substring is not unique
                else:
                    chars += c  # Add new unique character to the list
            return True  # If all characters in the substring are unique

        lengths = []  # List to store lengths of all unique substrings found
        start_pointer = 0  # Start pointer of the sliding window
        end_pointer = 1  # End pointer of the sliding window, starts at 1 to include at least one character

        # Edge case: if string is empty or contains only one character
        if len(s) in [0,1]:
            return len(s)  # Return the length of the string since it's either 0 or 1

        # Main loop to slide the window across the string
        while end_pointer != len(s):
            substr = s[start_pointer:end_pointer]  # Current substring from start to end pointer
            if isUnique(substr):
                lengths.append(len(substr))  # If substring is unique, store its length
            else:
                start_pointer += 1  # If not unique, move the start pointer to the right to exclude the repeated character
            end_pointer += 1  # Always move the end pointer to the right to explore new substrings

        # Final check for the last substring when end_pointer reaches the end of the string
        substr = s[start_pointer:end_pointer]
        if isUnique(substr):
            lengths.append(len(substr))  # Check uniqueness of the final substring

        return max(lengths)  # Return the maximum length found among all unique substrings
