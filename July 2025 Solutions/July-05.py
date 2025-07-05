class Solution:
    def maxSum(self, arr):
        max_score = 0
        for i in range(len(arr) - 1):
            score = arr[i] + arr[i + 1]
            max_score = max(max_score, score)
        return max_score
