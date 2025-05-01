class Solution:

    def nthRowOfPascalTriangle(self, n):
        MOD = 10**9 + 7
        row = [1]  
        
        for i in range(1, n):
            next_val = (row[-1] * (n - i) // i) % MOD
            row.append(next_val)
        
        return row
