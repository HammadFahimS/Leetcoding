# Integer to Roman

#### Problem Statement
The "Integer to Roman" problem (LeetCode #12) requires converting an integer to a Roman numeral. Roman numerals are represented by combinations of letters from the Latin alphabet (I, V, X, L, C, D, M) representing specific values. The challenge is to create a Roman numeral that correctly represents the input integer using the subtraction rule and concatenation of these symbols.

#### Solution Overview
The solution uses a greedy approach facilitated by mapping specific values to their Roman numeral representations. It iteratively reduces the integer by subtracting the largest possible Roman numeral values, appending the corresponding symbols to the result string until the entire integer is converted.

#### Detailed Explanation
1. **Initialization**:
   - A string `roman` is initialized to build the Roman numeral.
   - A list `mapping` stores tuples of integer values and their corresponding Roman numeral symbols, sorted in descending order.

2. **Conversion Process**:
   - The function iterates over the `mapping` list.
   - For each value and symbol in `mapping`, while the current integer (`num`) is greater than or equal to the value, the symbol is appended to `roman`, and the value is subtracted from `num`.

3. **Termination**:
   - The loop continues until the integer is reduced to zero.

#### Example Calculation:
Consider the integer `1994`. The conversion process would be as follows:

| Step | Value | Roman | Result  | Remaining Num |
|------|-------|-------|---------|---------------|
| 1    | 1000  | M     | M       | 994           |
| 2    | 900   | CM    | MCM     | 94            |
| 3    | 90    | XC    | MCMXC   | 4             |
| 4    | 4     | IV    | MCMXCIV | 0             |


#### Time and Space Complexities
- **Time Complexity**: \(O(1)\), as the mapping and iterations are limited and do not grow with the size of the input.
- **Space Complexity**: \(O(1)\), since the output size is constant regardless of the input size.

#### Results
- **Runtime**: 26 ms, faster than 75.51% of Python submissions.
- **Memory Usage**: 11.77 MB, less efficient than 6.60% of submissions.

#### Example Usage
```python
num = 1994
solution = Solution()
print(solution.intToRoman(num))  # Output: MCMXCIV
```

#### Contributions
Your contributions to optimizing or improving this implementation are welcome. Feel free to fork this project, make your changes, and submit a pull request.

#### License
This project is open-sourced under the MIT license. Feel free to use it as per the terms of the license.

---
