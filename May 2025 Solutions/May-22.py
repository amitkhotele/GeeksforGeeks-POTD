class Solution:
    def minDeletions(self, s):
        n = len(s)
        # Create a DP table for LPS
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Build the table
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        lps_length = dp[0][n - 1]
        return n - lps_length
