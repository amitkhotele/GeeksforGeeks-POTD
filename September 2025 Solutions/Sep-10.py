class Solution:
    def largestSwap(self, s: str) -> str:
        n = len(s)
        s = list(s)  # convert to list for easy swapping

        # Step 1: find the rightmost maximum digit for each position
        max_right = [-1] * n
        max_idx = n - 1
        for i in range(n - 1, -1, -1):
            if s[i] > s[max_idx]:
                max_idx = i
            max_right[i] = max_idx

        # Step 2: find the first place where swap improves the string
        for i in range(n):
            if s[i] < s[max_right[i]]:
                # swap
                s[i], s[max_right[i]] = s[max_right[i]], s[i]
                return "".join(s)

        # Step 3: if no swap, return original
        return "".join(s)
