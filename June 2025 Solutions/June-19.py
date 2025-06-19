class Solution:
    def caseSort(self, s):
        upper = sorted([ch for ch in s if ch.isupper()])
        lower = sorted([ch for ch in s if ch.islower()])
        
        result = []
        u = l = 0  # Pointers for uppercase and lowercase lists

        for ch in s:
            if ch.isupper():
                result.append(upper[u])
                u += 1
            else:
                result.append(lower[l])
                l += 1

        return ''.join(result)
