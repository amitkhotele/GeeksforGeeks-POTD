class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        # Transform the array
        transformed = [1 if num > k else -1 for num in arr]

        prefix_sum = 0
        first_occurrence = {}
        max_len = 0

        for i in range(n):
            prefix_sum += transformed[i]

            # If sum > 0, the subarray from 0 to i is valid
            if prefix_sum > 0:
                max_len = i + 1
            else:
                # Check if (prefix_sum - 1) occurred before
                if (prefix_sum - 1) in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[prefix_sum - 1])

            # Store the first occurrence of this prefix_sum
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len
