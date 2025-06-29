class Solution:
    def splitArray(self, arr, k):
        def is_valid(mid):
            count = 1
            curr_sum = 0
            for num in arr:
                if curr_sum + num > mid:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return count <= k

        left, right = max(arr), sum(arr)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
