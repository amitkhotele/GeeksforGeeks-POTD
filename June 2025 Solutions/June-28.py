from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        # Sort array b[] to enable binary search
        b.sort()
        result = []
        
        for x in a:
            # bisect_right gives index of the first element greater than x
            # So, all elements at indices < this value are <= x
            count = bisect_right(b, x)
            result.append(count)
        
        return result
