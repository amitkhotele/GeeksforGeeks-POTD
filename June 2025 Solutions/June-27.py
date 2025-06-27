class Solution:
    def getCount(self, n):
        if n == 1:
            return 10

        # Neighbors map including self
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }

        # Initialize dp table
        dp = [[0] * (n + 1) for _ in range(10)]

        # Base case
        for i in range(10):
            dp[i][1] = 1

        # Fill dp table
        for k in range(2, n + 1):
            for i in range(10):
                dp[i][k] = 0
                for nei in moves[i]:
                    dp[i][k] += dp[nei][k - 1]

        # Total count from all starting digits
        total = sum(dp[i][n] for i in range(10))
        return total
