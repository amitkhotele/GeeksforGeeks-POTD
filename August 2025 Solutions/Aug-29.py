from collections import Counter

class Solution:
    def smallestWindow(self, s, p):
        if not s or not p or len(p) > len(s):
            return ""
        
        # Step 1: Count frequencies in p
        need = Counter(p)
        required = len(need)  # unique chars to match
        
        # Sliding window setup
        left = 0
        formed = 0
        window_counts = {}
        
        # Answer tuple -> (window_length, left, right)
        ans = (float("inf"), 0, 0)
        
        # Step 2: Expand with right pointer
        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if current char satisfies one needed requirement
            if char in need and window_counts[char] == need[char]:
                formed += 1
            
            # Step 3: Try shrinking from left when all chars matched
            while left <= right and formed == required:
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Shrink window
                window_counts[s[left]] -= 1
                if s[left] in need and window_counts[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
        
        # Step 4: Return result
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
