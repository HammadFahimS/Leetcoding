class Solution(object):
    def isMatch(self, s, p):
        # Initialize the DP table with False
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Base case: empty string and empty pattern are a match
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c* that can match an empty string
        for j in range(2, len(p) + 1):
            dp[0][j] = dp[0][j-2] if p[j-1] == '*' else False

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    # Check zero occurrence or more occurrence
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] if p[j-2] == s[i-1] or p[j-2] == '.' else False)
                else:
                    # Direct match or match with '.'
                    dp[i][j] = dp[i-1][j-1] if p[j-1] == s[i-1] or p[j-1] == '.' else False

        # Return the value in the bottom-right corner of the table
        return dp[len(s)][len(p)]
