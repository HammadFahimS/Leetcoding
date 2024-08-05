class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Map each digit to the corresponding letters as per the typical mobile keypad.
        mapping = {'':[],
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }
        
        # Get the length of the input digits string.
        length = len(digits)
        
        # Handle the case where the length is less than 2.
        if length < 2:
            return mapping[digits]  # Directly return the mapped letters for the single digit.

        # Initialize a list to store the combinations starting with an empty string.
        multiplied = ['']
        
        # Iterate through each character in the input digits.
        for char in digits:
            # Create new combinations by appending each possible letter (mapped from the current digit)
            # to each of the existing combinations stored in 'multiplied'.
            multiplied = [x + y for x in multiplied for y in mapping[char]]
        
        # Return the list of all combinations formed.
        return multiplied
