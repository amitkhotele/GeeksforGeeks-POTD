class Solution:
    def maxKPower(self, n, k):
        def prime_factors(k):
            factors = {}
            i = 2
            while i * i <= k:
                while k % i == 0:
                    factors[i] = factors.get(i, 0) + 1
                    k //= i
                i += 1
            if k > 1:
                factors[k] = 1
            return factors
        
        def count_factor_in_factorial(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count
        
        factors = prime_factors(k)
        min_power = float('inf')

        for p, a in factors.items():
            count = count_factor_in_factorial(n, p)
            min_power = min(min_power, count // a)
        
        return min_power
