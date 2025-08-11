class Solution:
    def maxSum(self, s: str) -> int:
        n = len(s)
        
        # Step 1: Manacher's for odd palindromes
        d1 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1
        
        # Step 2: Fill maxEnd and maxStart for all ends/starts
        maxEnd = [0] * n
        maxStart = [0] * n
        for center in range(n):
            radius = d1[center]
            start = center - radius + 1
            end = center + radius - 1
            # This is the largest one for this center
            if 2 * radius - 1 > maxEnd[end]:
                maxEnd[end] = 2 * radius - 1
            if 2 * radius - 1 > maxStart[start]:
                maxStart[start] = 2 * radius - 1
        
        # Step 3: Propagate to cover smaller palindromes inside big ones
        # Left propagation for maxEnd
        for i in range(n - 1):
            if maxEnd[i] > 1:
                # smaller palindrome also ends at i-2, i-4, ...
                maxEnd[i - 2 if i >= 2 else 0] = max(maxEnd[i - 2 if i >= 2 else 0], maxEnd[i] - 2)
        
        # Propagate to make sure every index knows the best ending there
        for i in range(1, n):
            maxEnd[i] = max(maxEnd[i], maxEnd[i - 1])

        # Right propagation for maxStart
        for i in range(n - 1, 0, -1):
            if maxStart[i] > 1:
                # smaller palindrome also starts at i+2, i+4, ...
                if i + 2 < n:
                    maxStart[i + 2] = max(maxStart[i + 2], maxStart[i] - 2)
        
        for i in range(n - 2, -1, -1):
            maxStart[i] = max(maxStart[i], maxStart[i + 1])

        # Step 4: Try every split
        ans = 0
        for cut in range(n - 1):
            ans = max(ans, maxEnd[cut] + maxStart[cut + 1])
        return ans
