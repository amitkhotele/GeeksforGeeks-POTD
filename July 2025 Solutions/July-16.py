import math

class Solution:
    def countNumbers(self, n):
        def sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(limit**0.5) + 1):
                if is_prime[i]:
                    for j in range(i*i, limit + 1, i):
                        is_prime[j] = False
            primes = [i for i, val in enumerate(is_prime) if val]
            return primes

        count = 0
        limit = int(n**0.5) + 1
        primes = sieve(limit)

        # Type 1: p^8
        for p in primes:
            if p**8 <= n:
                count += 1
            else:
                break

        # Type 2: p^2 * q^2
        len_primes = len(primes)
        for i in range(len_primes):
            for j in range(i + 1, len_primes):
                num = (primes[i]**2) * (primes[j]**2)
                if num <= n:
                    count += 1
                else:
                    break

        return count
