class Solution:
    def countConsec(self, n: int) -> int:
        # Arrays to store number of valid strings ending in 0 and 1
        a = [0] * (n + 1)
        b = [0] * (n + 1)

        # Base cases
        a[1] = 1
        b[1] = 1

        for i in range(2, n + 1):
            a[i] = a[i - 1] + b[i - 1]
            b[i] = a[i - 1]

        good = a[n] + b[n]
        total = 2 ** n
        bad = total - good

        return bad
