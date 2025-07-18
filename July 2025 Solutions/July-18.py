import math

class Solution:
    def lcmTriplets(self, n):
        def lcm(a, b):
            return a * b // math.gcd(a, b)
        
        def lcm3(a, b, c):
            return lcm(lcm(a, b), c)

        if n <= 2:
            return n

        max_lcm = 0
        # Try all combinations of triplets in the range [n, n-5] for maximum LCM
        for i in range(n, max(n - 6, 0), -1):
            for j in range(n, max(n - 6, 0), -1):
                for k in range(n, max(n - 6, 0), -1):
                    if i != j and j != k and i != k:
                        max_lcm = max(max_lcm, lcm3(i, j, k))
        
        return max_lcm
