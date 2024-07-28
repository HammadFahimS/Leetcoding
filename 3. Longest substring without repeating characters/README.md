# Longest Substring Without Repeating Characters
#### Problem Statement
This repository contains a Python solution for the coding challenge "Longest Substring Without Repeating Characters". The challenge is to find the length of the longest substring without repeating characters from a given string.

#### Example
Input: "abcabcbb"
Output: 3 (The answer is "abc", with the length of 3.)

#### Solution Description
The solution employs a sliding window technique with two pointers, start_pointer and end_pointer, to efficiently explore potential substrings within the input string. It uses a helper function isUnique to verify if the substring has all unique characters. If a repetition is detected, the start_pointer is moved right to exclude the repeating character, effectively resizing the window to skip over the problematic character.

#### Key Features
Efficiency: Utilizes a sliding window approach to minimize unnecessary checks, aiming for an optimal solution in terms of runtime.
Simplicity: The implementation focuses on clarity and readability, making it accessible for users new to the sliding window technique.

#### Results
Runtime: 1371 ms, which beats 9.68% of Python submissions.
Memory Usage: 11.89 MB, which is better than 77.18% of Python submissions.

#### Usage
To use this solution, simply clone the repository and run the script with Python. Ensure that your environment is set up with Python 3.

#### Contributions
Contributions to improve the solution are welcome, especially those that could further optimize the approach or reduce the memory footprint.

#### License
This project is released under the MIT License.
