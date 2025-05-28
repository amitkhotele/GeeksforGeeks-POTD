class Solution:    
    def ValidCorner(self, mat): 
        n = len(mat)
        m = len(mat[0])
        
        # Set to store seen column pairs
        seen_pairs = set()
        
        for i in range(n):
            ones_in_row = []
            for j in range(m):
                if mat[i][j] == 1:
                    ones_in_row.append(j)
            
            # Check all pairs of columns in this row that have 1s
            for c1 in range(len(ones_in_row)):
                for c2 in range(c1 + 1, len(ones_in_row)):
                    pair = (ones_in_row[c1], ones_in_row[c2])
                    if pair in seen_pairs:
                        return True
                    seen_pairs.add(pair)
        
        return False
