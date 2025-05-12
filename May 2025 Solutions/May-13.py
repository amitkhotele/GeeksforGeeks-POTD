class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        
        MOD = 10**9 + 7  # Not required here, but common in problems with large values
        
        # Initialize a table of size (n+1) x (r+1)
        dp = [[0] * (r + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(min(i, r) + 1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        return dp[n][r]

