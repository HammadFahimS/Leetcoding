# Roman to Integer

#### Problem Statement
The "Roman to Integer" problem (LeetCode #13) requires converting a Roman numeral string to its integer equivalent. Roman numerals are represented by combinations of letters from the Latin alphabet that signify specific values. The notation combines these symbols and applies the subtractive principle for particular patterns, making the conversion from Roman numerals to integers not entirely straightforward.

#### Solution Overview
This solution uses a mapping strategy that involves processing the Roman numeral string from right to left. Iterating backwards allows the direct application of Roman numeral rules, especially handling subtractive combinations effectively by checking preceding characters.

#### Detailed Explanation
- **Mapping Dictionary**: A dictionary is initialized containing all relevant Roman numerals and their integer values, including subtractive sequences like "IV" and "IX".
- **Reverse Iteration**: The string is processed from the end to the beginning to directly handle subtraction when a smaller numeral precedes a larger numeral.
- **Calculation**: For each character, the numeral's value is added to the total unless a subtractive rule is identified, in which case the numeral's value is subtracted.

#### Step-by-Step Conversion Example: 'MCMXCIV' to 1994
The following table illustrates the conversion of 'MCMXCIV' to 1994 by processing each character from right to left:

| Character | Value | Cumulative Total | Operation | Explanation |
|-----------|-------|------------------|-----------|-------------|
| V         | 5     | 5                | Add       | Start with V; no previous numeral, add 5 |
| I         | 1     | 4                | Subtract       | V > I, subtract 1 |
| C         | 100   | 104              | Add       | C > V, add 100 |
| X         | 10    | 94               | Subtract  | C > X, previous C causes subtraction of 10 |
| M         | 1000  | 1094             | Add       | M > C, add 1000 |
| C         | 100   | 994              | Subtract  | M > C, previous M causes subtraction of 100 |
| M         | 1000  | 1994             | Add       | Start is M and no previous, add 1000 |

Final Result: 1994

#### Code Implementation
```python
class Solution:
    def romanToInt(self, s):
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for char in reversed(s):
            value = mapping[char]
            if value >= prev_value:
                total += value
            else:
                total -= value
            prev_value = value
        return total
```

#### Complexity Analysis
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the Roman numeral string. Each character is processed once.
- **Space Complexity**: \(O(1)\). The space used does not scale with the input size, and only a few auxiliary variables are used.

#### Performance Metrics
- **Runtime**: 21 ms, beating 90.67% of Python submissions, which indicates a highly efficient implementation.
- **Memory Usage**: 11.60 MB, which is better than 78.15% of Python submissions.

#### Contributions
Contributions to further optimize or refine this solution are welcome. Feel free to fork this repository, make your changes, and submit a pull request.

---
