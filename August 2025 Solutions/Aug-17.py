class Solution:
    def rearrange(self, arr, x):
        # Stable sort by absolute difference with x
        arr.sort(key=lambda num: abs(num - x))
        return arr
