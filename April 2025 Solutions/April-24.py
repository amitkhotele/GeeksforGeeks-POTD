class Solution:
    def getSingle(self, arr):
        result = 0
        
        for i in range(32):  # iterate over 32 bits
            bit_sum = 0
            for num in arr:
                if (num >> i) & 1:
                    bit_sum += 1
            if bit_sum % 3 != 0:
                # If it's the sign bit (31st), handle negative values
                if i == 31:
                    result -= (1 << 31)
                else:
                    result |= (1 << i)
        
        return result
