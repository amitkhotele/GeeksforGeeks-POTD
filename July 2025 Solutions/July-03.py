class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        if k == 0 or n == 0:
            return -1
        
        char_freq = {}
        max_len = -1
        start = 0
        
        for end in range(n):
            # Include current character in the window
            char_freq[s[end]] = char_freq.get(s[end], 0) + 1
            
            # Shrink the window until we have at most k distinct characters
            while len(char_freq) > k:
                char_freq[s[start]] -= 1
                if char_freq[s[start]] == 0:
                    del char_freq[s[start]]
                start += 1
            
            # Check if window has exactly k unique characters
            if len(char_freq) == k:
                max_len = max(max_len, end - start + 1)
        
        return max_len
