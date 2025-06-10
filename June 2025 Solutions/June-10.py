import collections

class Solution:
    def countStrings(self, s):
        n = len(s)
        
        char_counts = collections.Counter(s)
        
        num_duplicate_pairs = 0
        has_duplicates_flag = False

        for count in char_counts.values():
            if count > 1:
                has_duplicates_flag = True
                num_duplicate_pairs += (count * (count - 1)) // 2
        
        total_possible_swaps = (n * (n - 1)) // 2
        
        ans = total_possible_swaps - num_duplicate_pairs
        
        if has_duplicates_flag:
            ans += 1
            
        return ans
