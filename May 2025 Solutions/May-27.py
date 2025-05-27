class Solution:
    def leafNodes(self, preorder):
        self.index = 0
        n = len(preorder)
        ans = []

        def dfs(min_val, max_val):
            if self.index >= n:
                return

            curr = preorder[self.index]
            if not (min_val < curr < max_val):
                return

            self.index += 1
            left_index = self.index
            dfs(min_val, curr)
            right_index = self.index
            dfs(curr, max_val)

            # If no left or right subtree was added => it's a leaf
            if left_index == right_index == self.index:
                ans.append(curr)

        dfs(float('-inf'), float('inf'))
        return ans
