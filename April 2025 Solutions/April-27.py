class Solution:
    def multiplyStrings(self, s1, s2):
        # Remove leading zeros
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')
        
        # Edge case: if either becomes empty, it was "0"
        if not s1 or not s2:
            return "0"
        
        # Handle negative numbers
        negative = False
        if s1[0] == '-' and s2[0] == '-':
            s1 = s1[1:]
            s2 = s2[1:]
        elif s1[0] == '-':
            negative = True
            s1 = s1[1:]
        elif s2[0] == '-':
            negative = True
            s2 = s2[1:]
        
        n, m = len(s1), len(s2)
        result = [0] * (n + m)  # maximum size possible
        
        # Multiply each digit
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                sum = mul + result[i + j + 1]
                
                result[i + j + 1] = sum % 10
                result[i + j] += sum // 10
        
        # Skip leading zeros
        res = []
        for num in result:
            if not (len(res) == 0 and num == 0):
                res.append(str(num))
        
        if not res:
            return "0"
        
        ans = ''.join(res)
        if negative:
            ans = '-' + ans
        return ans
