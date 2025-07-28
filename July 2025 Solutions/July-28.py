class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[i][j] for i in range(n)) for j in range(n)]
        
        # Find the maximum sum among all rows and columns
        target = max(max(row_sum), max(col_sum))
        
        total_ops = 0
        
        for i in range(n):
            total_ops += target - row_sum[i]
        
        return total_ops
