from collections import Counter
import heapq

class Solution:
    def validgroup(self, arr, k):
        if len(arr) % k != 0:
            return False  # total number of balls not divisible by k
        
        count = Counter(arr)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]  # Get the smallest number
            for i in range(first, first + k):
                if count[i] == 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    # If frequency becomes 0, remove from heap
                    if i != min_heap[0]:
                        continue
                    heapq.heappop(min_heap)
                    while min_heap and count[min_heap[0]] == 0:
                        heapq.heappop(min_heap)
        
        return True
