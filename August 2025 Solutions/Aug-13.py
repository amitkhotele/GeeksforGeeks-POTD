import math

class Solution:
    def minSoldiers(self, arr, k):
        n = len(arr)
        lucky_count = 0
        add_list = []
        
        for soldiers in arr:
            if soldiers % k == 0:
                lucky_count += 1
            else:
                add_list.append(k - (soldiers % k))
        
        # Already enough lucky troops
        if lucky_count >= math.ceil(n / 2):
            return 0
        
        # Sort required additions
        add_list.sort()
        
        # Number of troops we still need to make lucky
        required = math.ceil(n / 2) - lucky_count
        
        # Sum smallest 'required' additions
        return sum(add_list[:required])
