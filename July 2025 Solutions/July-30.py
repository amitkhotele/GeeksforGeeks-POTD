class Solution:
    def cntSubarrays(self, arr, k):
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  # to handle the case when prefix_sum == k

        for num in arr:
            prefix_sum += num
            if (prefix_sum - k) in prefix_map:
                count += prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count
