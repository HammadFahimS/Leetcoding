class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Initialize a boolean to check if the original number is negative
        signed = False
        if x < 0:
            signed = True  # Set the flag if the number is negative
            x = x * -1  # Make the number positive for ease of manipulation
        
        # Variable to store the reversed integer
        reversed = 0
        # Continue extracting digits until x is less than 10
        while x >= 10:
            digit = int(x % 10)  # Get the last digit of x
            reversed = reversed * 10 + digit  # Append the digit to the reversed number
            x = int(x / 10)  # Remove the last digit from x
        
        # Add the last digit
        reversed = reversed * 10 + x
        
        # If the number was originally negative, convert the result back to negative
        if signed:
            reversed = reversed * -1
        
        # Check for 32-bit integer overflow
        if pow(-2, 31) > reversed or reversed > pow(2, 31) - 1:
            return 0  # Return 0 if overflow occurs
        
        # Return the reversed integer if no overflow
        return reversed
