class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        candidate = -1
        count = 0

        # Step 1: Find a potential candidate
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Step 2: Verify the candidate
        if arr.count(candidate) > n // 2:
            return candidate
        else:
            return -1
