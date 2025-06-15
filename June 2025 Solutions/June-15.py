import math

class Solution:
    def smallestDivisor(self, arr, k):
        def compute_sum(divisor):
            return sum((math.ceil(num / divisor) for num in arr))
        
        left = 1
        right = max(arr)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if compute_sum(mid) <= k:
                answer = mid
                right = mid - 1  # try to find a smaller divisor
            else:
                left = mid + 1  # increase divisor to reduce the sum
        
        return answer
