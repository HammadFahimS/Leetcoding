class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Dictionary to hold characters for each row of the zigzag pattern
        chars_per_line = {x+1: [] for x in range(numRows)}
        
        # Initial state to control the direction of zigzag pattern traversal
        currLine = 1  # Start from the first row
        goingDown = True  # Initial direction is down
        goingUp = False  # Not going up initially
        
        # If only one row, return the original string as zigzag conversion is not needed
        if numRows == 1:
            return s
        
        # Iterate over each character in the string
        for char in s:
            # Append the current character to the list corresponding to the current row
            chars_per_line[currLine].append(char)
            
            # Logic to change direction when the bottom or top is reached
            if currLine == numRows:  # If current line is the last row
                goingDown = False
                goingUp = True
            if currLine == 1:  # If current line is the first row
                goingDown = True
                goingUp = False
            
            # Update the current row based on the direction of traversal
            if goingDown:
                currLine += 1
            if goingUp:
                currLine -= 1
        
        # Construct the zigzag string from characters stored in dictionary rows
        zigzag = ""
        for k, v in chars_per_line.items():
            # Concatenate characters in each row in order
            for char in v:
                zigzag += char
        
        # Print the content of each row for debugging (can be removed in production)
        print(chars_per_line)
        
        return zigzag
