class Solution:
    def getLongestPrefix(self, s):
        n = len(s)

        # Step 1: Build Z-array
        Z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] - 1 > r:
                l, r = i, i + Z[i] - 1

        # Step 2: Check largest prefix length
        for L in range(n - 1, 0, -1):
            ok = True
            for i in range(L, n, L):
                if Z[i] < min(L, n - i):
                    ok = False
                    break
            if ok:
                return L
        return -1
