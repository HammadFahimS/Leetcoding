class Solution(object):
    def myAtoi(self, s):
        # Helper function to check and adjust the number if it's beyond the 32-bit integer limits
        def returnChecks(number, ll, ul):
            if number < ll:
                return ll  # Return lower limit if underflow
            if number > ul:
                return ul  # Return upper limit if overflow
            return number  # Return the number if within the bounds

        # Define 32-bit signed integer range
        lower_limit = -2**31
        upper_limit = 2**31 - 1
        
        # Strip leading/trailing whitespaces
        s = s.strip()
        # Handle the case where string is empty after stripping
        if s == "":
            return 0
        
        # Default sign is positive
        sign = "+"
        number = 0
        # Check if the first character is a sign
        if s[0] == '-' or s[0] == '+':
            sign = s[0]  # Set the sign
            # Process the characters after the sign
            for character in s[1:]:
                if character.isdigit():  # Convert digit characters to integers
                    number = number * 10 + int(character)
                else:
                    break  # Stop processing if a non-digit character is encountered
            if sign == '-':
                number = -number  # Apply the sign to the number
            return returnChecks(number, lower_limit, upper_limit)  # Check range and return
        
        # If no sign is present, process all characters
        for character in s:
            if character.isdigit():
                number = number * 10 + int(character)
            else:
                break
        # Apply the sign if negative
        if sign == '-':
            number = -number
        return returnChecks(number, lower_limit, upper_limit)  # Check range and return
