class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        # Start with the first element of the sequence
        result = "1"
        
        # Generate sequence up to the nth term
        for _ in range(2, n + 1):
            current = ""
            i = 0
            while i < len(result):
                count = 1
                # Count consecutive characters
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1
                # Append count followed by digit
                current += str(count) + result[i]
                i += 1
            result = current
        
        return result
