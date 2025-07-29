class Solution:
    def asciirange(self, s):
        first_last = {}
        result = []
        
        for i, ch in enumerate(s):
            if ch not in first_last:
                first_last[ch] = [i, i]
            else:
                first_last[ch][1] = i

        for ch, (first, last) in first_last.items():
            if first != last:
                ascii_sum = sum(ord(s[i]) for i in range(first + 1, last))
                if ascii_sum != 0:
                    result.append(ascii_sum)

        return result
