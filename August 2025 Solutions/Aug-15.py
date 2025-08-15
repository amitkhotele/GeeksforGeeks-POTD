class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        inserted = False
        
        for interval in intervals:
            # Case 1: interval ends before newInterval starts → no overlap
            if interval[1] < newInterval[0]:
                result.append(interval)
            
            # Case 2: interval starts after newInterval ends → no overlap
            elif interval[0] > newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append(interval)
            
            # Case 3: Overlap → merge intervals
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # If newInterval is still not inserted
        if not inserted:
            result.append(newInterval)
        
        return result
