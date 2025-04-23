class Solution:
    def singleNum(self, arr):
        xor = 0
        for num in arr:
            xor ^= num
        
        # Find rightmost set bit
        set_bit = xor & -xor
        
        num1 = 0
        num2 = 0
        
        # Divide numbers into two groups based on the set bit
        for num in arr:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return sorted([num1, num2])
