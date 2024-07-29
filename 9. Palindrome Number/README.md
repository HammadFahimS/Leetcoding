# Palindrome Number

#### Problem Statement
The "Palindrome Number" problem on LeetCode requires determining whether an integer is a palindrome without using extra space for converting the number into a string or array. A palindrome is a number that reads the same backward as forward, such as 121 or 12321.

#### Solution Overview
The solution provided involves converting the integer to a string and using two-pointer technique to check for symmetry, verifying whether the integer reads the same from both ends. The focus is on efficiency and correctness, ensuring that the approach works for all integer ranges supported in Python.

#### Detailed Explanation
1. **Initial Checks:** If the number is a single-digit (between 0 and 9), it is immediately returned as a palindrome. This is a simple check that quickly handles a common case.
2. **String Conversion:** The integer is converted to a string to utilize Python's string indexing capabilities, which simplifies character comparisons.
3. **Two-Pointer Technique:** Two pointers are initialized at the start and end of the string. These pointers move towards each other, and at each step, the characters at these pointers are compared. If any pair of characters does not match, the function returns `False`.
4. **Final Decision:** If the loop completes without finding mismatches, the function returns `True`, confirming the number is a palindrome.

#### Code Implementation
```python
class Solution(object):
    def isPalindrome(self, x):
        if 0 <= x < 10:
            return True  # Single digit numbers are always palindromes
        
        num = str(x)  # Convert the integer to a string
        length = len(num)
        
        # Compare characters from both ends moving towards the center
        for i in range(length // 2):
            if num[i] != num[length - 1 - i]:
                return False  # If mismatch is found, it's not a palindrome
        
        return True  # If no mismatches are found, it's a palindrome
```

#### Complexity Analysis
- **Time Complexity:** The time complexity is \(O(n)\), where \(n\) is the number of digits in the integer. Each digit is checked once up to the middle of the string.
- **Space Complexity:** The space complexity is \(O(1)\) if we disregard the space used for converting the integer to a string, as the space used does not scale with the input size.

#### Results
- **Runtime:** 34 ms, which places the solution in the top 80.02% of all Python submissions. This indicates an efficient approach that handles the problem quickly for most cases.
- **Memory Usage:** 11.48 MB, ranking better than 87.99% of Python submissions. This showcases the solution's minimal memory use, adhering to the problem's constraints to avoid extra space.

#### Usage
The solution can be tested directly on the LeetCode platform or integrated into any Python environment by including the `Solution` class and invoking the `isPalindrome` method:
```python
sol = Solution()
print(sol.isPalindrome(121))  # Output: True
print(sol.isPalindrome(-121)) # Output: False
```

#### Contributions
Contributions to improve the solution are welcome, especially those that could further optimize the approach or reduce the memory footprint.

#### License
This project is released under the MIT License.

---
