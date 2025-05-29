class Solution:
    def sumOfLongRootToLeafPath(self, root):
        self.maxSum = 0
        self.maxLen = 0

        def dfs(node, current_sum, current_len):
            if not node:
                return
            
            current_sum += node.data
            current_len += 1
            
            # If it's a leaf node
            if not node.left and not node.right:
                if current_len > self.maxLen:
                    self.maxLen = current_len
                    self.maxSum = current_sum
                elif current_len == self.maxLen:
                    self.maxSum = max(self.maxSum, current_sum)
                return
            
            dfs(node.left, current_sum, current_len)
            dfs(node.right, current_sum, current_len)
        
        dfs(root, 0, 0)
        return self.maxSum
