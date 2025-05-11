from typing import List


import heapq

class Solution:
    def kthLargest(self, arr, k) -> int:
        n = len(arr)
        min_heap = []

        # Generate all subarray sums
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += arr[j]
                heapq.heappush(min_heap, sum_)
                if len(min_heap) > k:
                    heapq.heappop(min_heap)  # remove smallest

        return min_heap[0]  # K-th largest sum
 
