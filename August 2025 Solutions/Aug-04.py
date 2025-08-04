class Solution:
    def maxRectSum(self, mat):
        if not mat:
            return 0
        
        n = len(mat)
        m = len(mat[0])
        max_sum = float('-inf')

        for left in range(m):
            temp = [0] * n  # Temporary row sum array
            
            for right in range(left, m):
                # Add the current column's values to each row
                for i in range(n):
                    temp[i] += mat[i][right]
                
                # Apply Kadane’s algorithm on temp[]
                curr_sum = temp[0]
                max_kadane = temp[0]
                for i in range(1, n):
                    curr_sum = max(temp[i], curr_sum + temp[i])
                    max_kadane = max(max_kadane, curr_sum)
                
                max_sum = max(max_sum, max_kadane)
        
        return max_sum
