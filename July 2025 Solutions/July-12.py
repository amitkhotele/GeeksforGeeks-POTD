class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n = len(mat)
        m = len(mat[0])
        
        # dp[i][j] will store the maximum gold collectable from cell (i, j) to the last column
        dp = [[0]*m for _ in range(n)]
        
        # Fill the last column with its own values
        for i in range(n):
            dp[i][m-1] = mat[i][m-1]
        
        # Fill the dp table from right to left
        for j in range(m-2, -1, -1):
            for i in range(n):
                # Move right
                right = dp[i][j+1]
                
                # Move right-up
                right_up = dp[i-1][j+1] if i > 0 else 0
                
                # Move right-down
                right_down = dp[i+1][j+1] if i < n-1 else 0
                
                dp[i][j] = mat[i][j] + max(right, right_up, right_down)
        
        # The result is the max value in the first column
        return max(dp[i][0] for i in range(n))
