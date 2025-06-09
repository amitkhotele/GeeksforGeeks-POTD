class Solution:
    def isDeadEnd(self, root):
        return self._checkDeadEnd(root, 1, float('inf'))
    
    def _checkDeadEnd(self, node, min_val, max_val):
        if not node:
            return False
        
        # If this is a leaf node
        if not node.left and not node.right:
            if min_val == max_val:
                return True
        
        # Recur for left and right subtree
        left = self._checkDeadEnd(node.left, min_val, node.data - 1)
        right = self._checkDeadEnd(node.right, node.data + 1, max_val)
        
        return left or right
