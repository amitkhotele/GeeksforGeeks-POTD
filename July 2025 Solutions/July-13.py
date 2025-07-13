class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        total_sum = sum(arr)
        
        # dp[i] stores length of LIS ending at i
        dp = [1] * n
        # sum_lis[i] stores minimum sum of LIS ending at i
        sum_lis = arr[:]  # Initially each element alone

        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        sum_lis[i] = sum_lis[j] + arr[i]
                    elif dp[j] + 1 == dp[i]:
                        sum_lis[i] = min(sum_lis[i], sum_lis[j] + arr[i])

        # LIS length
        max_len = max(dp)

        # Among all subsequences with that LIS length, find the one with minimum sum
        min_sum_lis = min(sum_lis[i] for i in range(n) if dp[i] == max_len)

        return total_sum - min_sum_lis
