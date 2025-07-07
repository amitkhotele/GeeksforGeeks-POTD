class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n  # Initialize result array with -1
        stack = []

        # Traverse the array twice to handle circular property
        for i in range(2 * n - 1, -1, -1):
            current = arr[i % n]
            # Pop elements that are smaller or equal to current
            while stack and stack[-1] <= current:
                stack.pop()
            # If in the first pass, update the result
            if i < n:
                if stack:
                    res[i] = stack[-1]
                else:
                    res[i] = -1
            stack.append(current)
        
        return res
