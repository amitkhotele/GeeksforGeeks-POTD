class Solution:
    def getLastMoment(self, n, left, right):
        max_left = max(left) if left else 0
        max_right = max((n - pos for pos in right), default=0)
        return max(max_left, max_right)
