class Solution:
    def substrCount(self, s, k):
        if k > len(s):
            return 0

        from collections import defaultdict
        
        count = 0
        freq = defaultdict(int)
        distinct = 0

        # Initialize first window
        for i in range(k):
            if freq[s[i]] == 0:
                distinct += 1
            freq[s[i]] += 1

        if distinct == k - 1:
            count += 1

        # Slide the window
        for i in range(k, len(s)):
            # Remove the character going out of window
            out_char = s[i - k]
            freq[out_char] -= 1
            if freq[out_char] == 0:
                distinct -= 1

            # Add the new character
            in_char = s[i]
            if freq[in_char] == 0:
                distinct += 1
            freq[in_char] += 1

            if distinct == k - 1:
                count += 1

        return count
