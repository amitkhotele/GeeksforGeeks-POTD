from collections import defaultdict
import heapq

class Solution:
    def sumOfModes(self, arr, k):
        n = len(arr)
        freq = defaultdict(int)          # frequency of numbers
        bucket = defaultdict(list)       # max heap for mode candidates per frequency
        maxFreq = 0
        result = 0
        
        def add(x):
            nonlocal maxFreq
            old = freq[x]
            freq[x] += 1
            new = freq[x]
            maxFreq = max(maxFreq, new)
            heapq.heappush(bucket[new], x)
        
        def remove(x):
            nonlocal maxFreq
            old = freq[x]
            if old == 0:
                return
            freq[x] -= 1
            # maxFreq might decrease later when bucket[maxFreq] becomes empty
            # lazy removal (don’t clean heaps immediately)
        
        def getMode():
            nonlocal maxFreq
            while maxFreq > 0:
                while bucket[maxFreq] and freq[bucket[maxFreq][0]] != maxFreq:
                    heapq.heappop(bucket[maxFreq])  # remove stale entries
                if bucket[maxFreq]:
                    return bucket[maxFreq][0]
                maxFreq -= 1
            return 0  # shouldn't happen
        
        # First window
        for i in range(k):
            add(arr[i])
        result += getMode()
        
        # Sliding windows
        for i in range(k, n):
            add(arr[i])
            remove(arr[i-k])
            result += getMode()
        
        return result
