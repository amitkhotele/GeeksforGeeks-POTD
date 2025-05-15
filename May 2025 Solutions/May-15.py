class Solution:
    def countSubstring(self, s):
        from collections import Counter

        freq = Counter(s)
        count = 0

        for ch in freq:
            n = freq[ch]
            count += (n * (n + 1)) // 2  # count of substrings starting and ending with same character

        return count

