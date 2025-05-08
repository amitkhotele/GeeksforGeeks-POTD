class Solution:
    def findMissing(self, arr):
        n = len(arr)
        # Step 1: Find correct common difference using min of consecutive diffs
        min_diff = float('inf')
        for i in range(1, n):
            min_diff = min(min_diff, arr[i] - arr[i - 1])
        
        # Step 2: Find where the difference is more than min_diff (i.e., missing spot)
        for i in range(1, n):
            if arr[i] - arr[i - 1] != min_diff:
                return arr[i - 1] + min_diff

        # Step 3: If no missing element found, return next element in AP
        return arr[-1] + min_diff

