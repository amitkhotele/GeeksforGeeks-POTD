class Solution:
    def findSubString(self, str):
        n = len(str)
        
        # Step 1: Count total distinct characters in the string
        distinct_chars = set(str)
        total_distinct = len(distinct_chars)
        
        # Step 2: Initialize variables
        freq_map = {}
        min_len = n  # At most the entire string
        start = 0
        count = 0  # To count distinct characters in current window
        
        for end in range(n):
            char = str[end]
            freq_map[char] = freq_map.get(char, 0) + 1
            
            # If this character's count becomes 1, we have a new distinct char in the window
            if freq_map[char] == 1:
                count += 1
            
            # Step 3: Try to shrink the window from the left
            while count == total_distinct:
                min_len = min(min_len, end - start + 1)
                
                # Shrink the window from left
                freq_map[str[start]] -= 1
                if freq_map[str[start]] == 0:
                    count -= 1
                start += 1
        
        return min_len
