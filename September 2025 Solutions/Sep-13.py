class Solution:
    def minCost(self, n, m, x, y):
        # Sort cuts in descending order
        x.sort(reverse=True)
        y.sort(reverse=True)
        
        i, j = 0, 0
        hz_segments, vt_segments = 1, 1
        total_cost = 0
        
        while i < len(x) and j < len(y):
            if x[i] >= y[j]:
                # Vertical cut
                total_cost += x[i] * hz_segments
                vt_segments += 1
                i += 1
            else:
                # Horizontal cut
                total_cost += y[j] * vt_segments
                hz_segments += 1
                j += 1
        
        # Remaining vertical cuts
        while i < len(x):
            total_cost += x[i] * hz_segments
            i += 1
            vt_segments += 1
        
        # Remaining horizontal cuts
        while j < len(y):
            total_cost += y[j] * vt_segments
            j += 1
            hz_segments += 1
        
        return total_cost
