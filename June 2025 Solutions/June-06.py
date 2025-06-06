class Solution:
    def search(self, pat, txt):
        M = len(pat)
        N = len(txt)
        d = 256  # number of characters in input alphabet
        q = 10**9 + 7  # A large prime number to mod hash values

        result = []

        # Pre-compute (d^(M-1)) % q
        h = 1
        for i in range(M-1):
            h = (h * d) % q

        # Compute hash value for pattern and first window of text
        p = 0  # hash value for pattern
        t = 0  # hash value for txt
        for i in range(M):
            p = (d * p + ord(pat[i])) % q
            t = (d * t + ord(txt[i])) % q

        # Slide the pattern over text
        for i in range(N - M + 1):
            # Check the hash values
            if p == t:
                # Check character by character
                if txt[i:i+M] == pat:
                    result.append(i + 1)  # 1-based index

            # Calculate hash for next window
            if i < N - M:
                t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
                if t < 0:
                    t += q

        return result
