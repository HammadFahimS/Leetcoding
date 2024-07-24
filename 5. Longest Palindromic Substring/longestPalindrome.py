class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Helper function to check if a given string is a palindrome
        def isPalindrome(subStr):
            end_ptr = len(subStr)-1  # Set a pointer at the end of the string
            for i in range(int(len(subStr)/2)):  # Loop through half of the string
                if subStr[i] != subStr[end_ptr]:  # Compare characters from start and end
                    return False  # If characters do not match, it's not a palindrome
                end_ptr -= 1  # Move the end pointer towards the start
            return True  # If all characters matched, it's a palindrome
    
        length = len(s)  # Length of the input string
        if isPalindrome(s):  # Check if the whole string is a palindrome
            return s  # Return the entire string if it's a palindrome

        # Dynamic programming table initialization
        dp = [[0 for i in range(length)] for j in range(length)]
        maxSubStr = ""  # Variable to store the longest palindrome found
        for i in range(length):  # Initialize single letter palindromes
            dp[i][i] = 1  # Every single character is a palindrome
            maxSubStr = s[i]  # Update maxSubStr to the latest single character

        for i in range(length-1):  # Initialize two consecutive letters as palindromes if they are the same
            if s[i] == s[i+1]:
                dp[i][i+1] = 1  # Set the dp table for two consecutive same letters
                maxSubStr = s[i:i+2]  # Update the longest palindrome to these two letters
        
        # Main loop to fill in the dp table for substrings longer than 2 characters
        for x in range(2, length):  # Start from size 3 to n
            for i in range(length):
                start = i
                end = i + x
                if end < length:  # Ensure the indices are within the string boundaries
                    if s[start] == s[end] and dp[start+1][end-1] == 1:
                        dp[start][end] = 1  # Mark this as a palindrome
                        subStr = s[start:end+1]  # Extract the substring
                        if len(subStr) > len(maxSubStr):  # Check if this palindrome is the longest found so far
                            maxSubStr = subStr  # Update maxSubStr with the longer palindrome
        return maxSubStr  # Return the longest palindromic substring found
