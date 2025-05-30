class Solution:
    def findMaxFork(self, root, k):
        res = -1
        while root:
            if root.data == k:
                return root.data
            elif root.data < k:
                res = root.data
                root = root.right
            else:
                root = root.left
        return res
