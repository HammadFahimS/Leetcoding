class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initialize an empty stack to keep track of opening parentheses.
        stack = []
        
        # Define a mapping from opening to closing parentheses.
        mapping = {'(': ')',
                   '{': '}',
                   '[': ']'}

        # Iterate over each character in the input string.
        for p in s:
            # If the character is an opening parenthesis, push it onto the stack.
            if p in mapping.keys():
                stack.append(p)
            
            # If the character is a closing parenthesis:
            if p in mapping.values():
                # Check if the stack is empty or if the top of the stack doesn't match the current closing parenthesis.
                if len(stack) == 0 or mapping[stack.pop()] != p:
                    return False  # Return False if the parentheses are not valid.

        # After processing all characters, check if the stack is empty.
        # If it's empty, all opening parentheses had matching closing ones.
        return len(stack) == 0
