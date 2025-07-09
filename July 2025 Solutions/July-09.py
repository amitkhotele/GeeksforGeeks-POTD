class Solution:
    def sumSubMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        
        # Previous Less Element
        prev = [0] * n
        stack = []
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            prev[i] = count

        # Next Less Element
        next_ = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            next_[i] = count
        
        # Final sum
        result = 0
        for i in range(n):
            result = (result + arr[i] * prev[i] * next_[i]) % MOD
        
        return result
