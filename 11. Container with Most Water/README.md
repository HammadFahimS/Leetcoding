# Container With Most Water

#### Problem Statement
The problem, known as "Container With Most Water", requires finding the maximum amount of water a container can store. This is determined by the vertical lines drawn on a number line, where the width of the container is the distance between the lines and the height is determined by the shorter of the two lines.

#### Solution Overview
The solution employs a two-pointer approach that starts at the boundaries of the line array and moves inward to determine the maximum area that can be formed between any two lines. This approach is efficient because it effectively reduces the problem space by eliminating cases that cannot possibly exceed the current maximum.

#### Detailed Explanation
1. **Initialization**:
   - `left_wall` is set to the index of the first line.
   - `right_wall` is set to the index of the last line.
   - `maximum` is initialized to 0 to keep track of the maximum area found.

2. **Processing**:
   - Calculate the area between `left_wall` and `right_wall` using the formula:
     \[
     \text{Area} = \min(\text{height}[left\_wall], \text{height}[right\_wall]) \times (right\_wall - left\_wall)
     \]
   - Update `maximum` if the newly calculated area is greater.
   - Move the pointer pointing to the shorter wall inward to potentially find a wall that allows a greater area.
   - If the heights are the same, move both pointers.

3. **Termination**:
   - The process repeats until the two pointers meet.

#### Example
Consider the heights array `height = [1,8,6,2,5,4,8,3,7]`. Let's illustrate the step-by-step computation:

| Step | Left Wall | Right Wall | Area Calculated | Maximum Area |
|------|-----------|------------|-----------------|--------------|
| 1    | 1         | 9          | 1 * (9-1) = 8   | 8            |
| 2    | 2         | 9          | 7 * (9-2) = 49  | 49           |
| 3    | 2         | 8          | 6 * (8-2) = 36  | 49           |
| ...  | ...       | ...        | ...             | ...          |

- As you can see, the pointers adjust based on the strategy described, and the areas are calculated accordingly.

#### Time and Space Complexities
- **Time Complexity**: \(O(n)\) where \(n\) is the number of elements in `height`. Each element is considered once when calculating the area.
- **Space Complexity**: \(O(1)\) as the space used does not depend on the input size and is constant.

#### Results
- **Runtime**: 514 ms, which beats 77.42% of Python submissions. This efficiency stems from the linear traversal of the height list.
- **Memory Usage**: 22.06 MB, better than 78.24% of Python submissions, reflecting minimal space usage beyond the input list.

#### Usage
```python
height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))  # Output will be the maximum water container area
```

#### Contributions
Contributions are welcome! Feel free to fork this repository, make enhancements, and submit a pull request. Whether it's optimizing the approach further or improving the readability of the code, your input is valued.

#### License
This project is shared for educational purposes. Use it as a learning tool or a base for your projects.

---
