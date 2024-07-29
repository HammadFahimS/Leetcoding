#Regular Expression Matching

#### Problem Statement
The "Regular Expression Matching" problem (LeetCode #10) challenges you to implement a function that supports regular expression matching with the characters '.' and '*', where:
- `'.'` Matches any single character.
- `'*'` Matches zero or more of the preceding element.

The function should match an entire string `s` to the pattern `p`.

#### Solution Overview
This solution uses a dynamic programming approach to solve the problem by constructing a 2D DP table `dp` where `dp[i][j]` is `True` if the first `i` characters of `s` match the first `j` characters of `p`. This approach handles the complexity of pattern matching involving the special characters '.' and '*'.

#### Detailed Step-by-Step Solution
To illustrate the dynamic programming approach, let's consider an example with `s = "aab"` and `p = "c*a*b"`.

##### Dynamic Programming Table Initialization:
1. Initialize a table `dp` with dimensions `(len(s)+1) x (len(p)+1)` filled with `False`. `dp[0][0]` is `True` because an empty string matches an empty pattern.
2. Handle patterns like `a*`, `a*b*` by setting `dp[0][j] = True` if `p[j-1] == '*'` and `dp[0][j-2]` is `True`.

##### Fill the DP Table:
- Here's how we fill the DP table based on the conditions mentioned:

| Match / Index | 0   | c   | *   | a   | *   | b   |
|---------------|-----|-----|-----|-----|-----|-----|
| **0**         | T   | F   | T   | F   | T   | F   |
| **a (1)**     | F   |     |     |     |     |     |
| **a (2)**     | F   |     |     |     |     |     |
| **b (3)**     | F   |     |     |     |     |     |

#### Example Calculation:
- Fill out the table from the initialized values and according to matching rules:
  - `dp[i][j] = dp[i-1][j-1]` if `p[j-1]` matches `s[i-1]` or if `p[j-1] == '.'`.
  - `dp[i][j] = dp[i][j-2]` if `p[j-1] == '*'` and the pattern segment up to `j-2` can match the segment of `s` up to `i`.
  - `dp[i][j] = dp[i-1][j]` if `p[j-1] == '*'` and `p[j-2]` matches `s[i-1]` or if `p[j-2] == '.'`.

Final Filled Table for `s = "aab"` and `p = "c*a*b"`:

| Match / Index | 0   | c   | *   | a   | *   | b   |
|---------------|-----|-----|-----|-----|-----|-----|
| **0**         | T   | F   | T   | F   | T   | F   |
| **a (1)**     | F   | F   | T   | F   | T   | F   |
| **a (2)**     | F   | F   | T   | F   | T   | F   |
| **b (3)**     | F   | F   | T   | F   | T   | T   |

#### Complexity Analysis:
- **Time Complexity:** O(m*n), where m is the length of the string `s` and n is the length of the pattern `p`.
- **Space Complexity:** O(m*n), due to the space required to store the DP table.

#### Performance Metrics:
- **Runtime:** 19 ms, beating 90.65% of Python submissions, indicating high efficiency.
- **Memory Usage:** 11.64 MB, better than 60.93% of submissions, showcasing good memory management.

#### Example Usage:
```python
s = "aab"
p = "c*a*b"
print(isMatch(s, p))  # Output: True
```

#### Contributions:
Contributions are welcome! If you have a more optimized solution or a clearer explanation, feel free to fork this repository and submit a pull request.

#### License:
This project is licensed under the MIT License.

---
