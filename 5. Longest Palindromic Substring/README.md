# Longest Palindromic Substring

#### Problem Statement
The "Longest Palindromic Substring" problem is a well-known challenge that asks for the longest contiguous substring of a given string that is also a palindrome. A palindrome reads the same backward as forward, and the goal is to identify the longest such substring in the provided string.

#### Solution Overview
This Python solution to the "Longest Palindromic Substring" utilizes dynamic programming to efficiently solve the problem by building a table that represents whether substrings are palindromic. The approach is based on the idea that a substring \( s[i:j] \) is a palindrome if \( s[i] \) equals \( s[j] \) and \( s[i+1:j-1] \) is a palindrome.

#### Detailed Explanation
1. **Dynamic Programming Table Initialization:** The solution initializes a 2D array `dp` where `dp[i][j]` is `True` if the substring from index `i` to `j` is a palindrome. It starts by marking all single-character substrings as palindromes.
2. **Building the DP Table:** The solution then considers substrings of length 2 and marks them as palindromic if both characters are the same. For substrings longer than 2, it uses the precomputed values to determine if the current substring is palindromic by checking the characters at the boundaries and the value of the inner substring.
3. **Tracking the Longest Palindrome:** While filling out the table, the solution keeps track of the longest palindrome found.

#### Complexity Analysis
- **Time Complexity:** The time complexity of this approach is \( O(n^2) \), where \( n \) is the length of the string. This is due to the necessity to fill a table of size \( n \times n \).
- **Space Complexity:** The space complexity is also \( O(n^2) \) because of the storage requirements of the DP table.

#### Results
- **Runtime:** 2451 ms, which places it in the 27.89 percentile among Python submissions. This indicates there is room for optimization, possibly by refining the condition checks or exploring alternative methods like expand around center or Manacher's algorithm.
- **Memory Usage:** 20.30 MB, placing it in the 5.70 percentile. This highlights the high memory demand due to the DP table, suggesting a potential improvement by considering space-efficient strategies.

#### Example Code Snippet
Here is a critical part of the implementation showing how the DP table is updated:
```python
for length in range(2, len(s) + 1):  # length of the substring
    for start in range(len(s) - length + 1):
        end = start + length - 1
        if s[start] == s[end] and (length == 2 or dp[start + 1][end - 1]):
            dp[start][end] = True
            if length > len(max_palindrome):
                max_palindrome = s[start:end + 1]
```

#### Contributions
Contributions to improve the solution are welcome, especially those that could further optimize the approach or reduce the memory footprint.

#### License
This project is released under the MIT License.
