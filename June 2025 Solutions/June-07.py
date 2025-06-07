class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        # Create a difference array
        diff = [a1[i] - a2[i] for i in range(n)]
        
        sum_map = {}  # Stores first occurrence of a prefix sum
        max_len = 0
        prefix_sum = 0
        
        for i in range(n):
            prefix_sum += diff[i]
            
            if prefix_sum == 0:
                max_len = i + 1  # whole subarray from 0 to i
            
            if prefix_sum in sum_map:
                # We have seen this sum before, calculate the length
                max_len = max(max_len, i - sum_map[prefix_sum])
            else:
                # Store the first occurrence
                sum_map[prefix_sum] = i
        
        return max_len
