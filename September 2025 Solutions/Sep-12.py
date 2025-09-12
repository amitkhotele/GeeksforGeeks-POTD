class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        # Initial difference
        ans = arr[-1] - arr[0]
        
        for i in range(1, n):
            if arr[i] - k < 0:
                continue  # skip negative height case
            
            # possible min and max
            smallest = min(arr[0] + k, arr[i] - k)
            largest = max(arr[i-1] + k, arr[-1] - k)
            
            ans = min(ans, largest - smallest)
        
        return ans
