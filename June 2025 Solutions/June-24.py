class Solution:
    def maxSubseq(self, s, k):
        n = len(s)
        keep = n - k
        stack = []
        
        for i, ch in enumerate(s):
            while stack and k > 0 and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        # Return only the first (n - k) characters
        return ''.join(stack[:keep])
