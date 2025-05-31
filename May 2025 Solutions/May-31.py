class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        
        def count_less_equal(mid):
            count = 0
            row, col = n - 1, 0  # Start from bottom-left
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count
        
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
