import heapq

class Solution:
    def printKClosest(self, arr, k, x):
        max_heap = []

        for num in arr:
            if num == x:
                continue
            # Using negative value to simulate a max-heap using Python's min-heap
            dist = abs(num - x)
            heapq.heappush(max_heap, (-dist, num))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Sort by custom rules: first by distance, then by value (prefer larger)
        result = sorted(max_heap, key=lambda t: (abs(t[1] - x), -t[1]))
        
        # Extract just the values
        return [val for _, val in result]

