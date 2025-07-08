from collections import Counter

class Solution:
    def findGreater(self, arr):
        n = len(arr)
        freq = Counter(arr)  # Get frequencies of elements
        res = [-1] * n       # Initialize result with -1
        stack = []           # Stack to keep elements (value, frequency)

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop elements from stack which have frequency less than or equal to current
            while stack and freq[stack[-1]] <= freq[arr[i]]:
                stack.pop()

            # If stack is not empty, top element has higher frequency
            if stack:
                res[i] = stack[-1]

            # Push current element onto stack
            stack.append(arr[i])

        return res
