class Solution:
    def countSubstr(self, s, k):
        return self.countAtMostK(s, k) - self.countAtMostK(s, k - 1)

    def countAtMostK(self, s, k):
        from collections import defaultdict
        freq = defaultdict(int)
        left = 0
        result = 0
        distinct = 0
        
        for right in range(len(s)):
            if freq[s[right]] == 0:
                distinct += 1
            freq[s[right]] += 1
            
            while distinct > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    distinct -= 1
                left += 1
            
            result += right - left + 1
        
        return result
