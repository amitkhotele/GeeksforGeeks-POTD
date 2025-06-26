import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        # Step 1: Count character frequencies
        freq = Counter(s)
        
        # Step 2: Max heap of frequencies (store as negative because heapq is min-heap)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)
        
        # Step 3: Perform k removals
        for _ in range(k):
            max_freq = heapq.heappop(max_heap)
            max_freq += 1  # Reducing frequency by 1 (remember it's negative)
            if max_freq < 0:
                heapq.heappush(max_heap, max_freq)
        
        # Step 4: Calculate the sum of squares (convert negatives back to positive)
        return sum((f * f) for f in max_heap)  # no need to multiply by -1
