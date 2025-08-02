class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        # Transform array to +1 and -1
        transformed = [1 if x > k else -1 for x in arr]

        prefix_sum = 0
        max_len = 0
        first_occurrence = {}

        for i in range(n):
            prefix_sum += transformed[i]

            if prefix_sum > 0:
                max_len = i + 1
            elif prefix_sum - 1 in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum - 1])
            
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i
        
        return max_len
