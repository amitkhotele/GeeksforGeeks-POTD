class Solution:
    def minDaysBloom(self, arr, k, m):
        n = len(arr)
        if m * k > n:  # Not enough flowers
            return -1

        def canMake(day):
            bouquets, count = 0, 0
            for bloom in arr:
                if bloom <= day:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0
            return bouquets >= m

        left, right = min(arr), max(arr)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if canMake(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
