# Valid Parenthesis

## Problem Statement

The **Valid Parenthesis** problem involves determining whether a given string of parentheses is valid. A string is considered valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Example

- **Input**: `s = "()"`  
  **Output**: `true`

- **Input**: `s = "()[]{}"`  
  **Output**: `true`

- **Input**: `s = "(]"`  
  **Output**: `false`

## Approach

To solve this problem, we use a stack data structure to keep track of the open parentheses encountered. We iterate over the string and apply the following logic:

1. If the current character is an open parenthesis (`(`, `{`, `[`), push it onto the stack.
2. If the current character is a close parenthesis (`)`, `}`, `]`), check the top element of the stack:
   - If the stack is empty, return `false`.
   - If the top of the stack is the corresponding open parenthesis for the current character, pop the top element from the stack.
   - Otherwise, return `false`.
3. After processing all characters, the stack should be empty if the string is valid.

### Code

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {'(': ')',
                   '{': '}',
                   '[': ']'}
        for p in s:
            if p in mapping.keys():
                stack.append(p)
            if p in mapping.values():
                if len(stack) == 0 or mapping[stack.pop()] != p:
                    return False
        return len(stack) == 0
```

## Complexity Analysis

### Time Complexity

- The time complexity of this solution is **O(n)**, where `n` is the length of the string. This is because we only make a single pass through the string, pushing and popping elements from the stack.

### Space Complexity

- The space complexity is **O(n)** in the worst case when all characters are open parentheses.

## Results

The solution was accepted with the following results:

- **Runtime**: 5 ms, faster than 98.31% of submissions.
- **Memory Usage**: 11.78 MB, better than 47.43% of submissions.

![Valid Parenthesis Result](file-DFyghQsUPsgKkk4dI9eUvG3k)

## Step-by-Step Illustration

| Step | Character | Stack           | Action                           |
|------|-----------|-----------------|----------------------------------|
| 1    | `(`       | `[` `(` `]`     | Push `(` onto stack              |
| 2    | `[`       | `[(` `[` `]`    | Push `[` onto stack              |
| 3    | `{`       | `[(` `[(` `]`   | Push `{` onto stack              |
| 4    | `}`       | `[(` `[(` `]`   | Pop `{`, matches `{`, continue   |
| 5    | `]`       | `[(` `[` `]`    | Pop `[`, matches `[`, continue   |
| 6    | `)`       | `[(` `]`        | Pop `(`, matches `(`, continue   |
| 7    | End       | `[]`            | Stack is empty, return `true`    |

---
