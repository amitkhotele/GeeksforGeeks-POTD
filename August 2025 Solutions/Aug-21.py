class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        
        def canPlace(d):
            # Greedy check if we can place k elements with at least d distance
            count = 1  # pick first element
            last = arr[0]
            for i in range(1, len(arr)):
                if arr[i] - last >= d:
                    count += 1
                    last = arr[i]
                if count >= k:
                    return True
            return False
        
        low, high = 0, arr[-1] - arr[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlace(mid):
                ans = mid
                low = mid + 1  # try larger minimum difference
            else:
                high = mid - 1  # try smaller
        return ans
