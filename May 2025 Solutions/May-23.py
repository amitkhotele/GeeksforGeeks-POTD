class Solution:
    def noOfWays(self, m, n, x):
        # Initialize a DP table
        dp = [[0] * (x + 1) for _ in range(n + 1)]

        # Base case: There's only one way to get sum j using one dice (j must be ≤ m)
        for j in range(1, min(m + 1, x + 1)):
            dp[1][j] = 1

        # Fill DP table
        for i in range(2, n + 1):  # Number of dice
            for j in range(1, x + 1):  # Target sum
                for k in range(1, min(m + 1, j)):  # Possible face values
                    dp[i][j] += dp[i - 1][j - k]

        return dp[n][x]
