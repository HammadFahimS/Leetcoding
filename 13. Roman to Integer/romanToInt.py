class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define a dictionary that maps all Roman numerals and their subtraction combinations to their integer values.
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                   'IV': 4, 'IX': 9,
                   'XL': 40, 'XC': 90,
                   'CD': 400, 'CM': 900}

        # Initialize total to accumulate the integer values.
        total = 0
        
        # Initialize previous_char to keep track of the last character in the loop.
        previous_char = ''
        
        # Loop through the string in reverse order to handle subtraction cases correctly.
        for character in s[::-1]:
            # Get the integer value of the current Roman numeral.
            num = mapping[character]
            
            # Check for the subtraction cases by comparing the current character with the previous one.
            # Subtract the value if the current numeral should be subtracted according to Roman numeral rules.
            if previous_char in ['V', 'X'] and character == 'I':
                total -= num
            elif previous_char in ['L', 'C'] and character == 'X':
                total -= num
            elif previous_char in ['D', 'M'] and character == 'C':
                total -= num
            else:
                # If no subtraction condition meets, add the value.
                total += num
            
            # Update the previous_char to the current character for the next iteration.
            previous_char = character

        # Return the total calculated value.
        return total
