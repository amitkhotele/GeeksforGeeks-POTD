class Solution:
    def findPreSuc(self, root, key):
        self.pre = None
        self.suc = None
        self._helper(root, key)
        return (self.pre, self.suc)
    
    def _helper(self, root, key):
        if not root:
            return
        
        # If root data is equal to key
        if root.data == key:
            # Predecessor is the rightmost of left subtree
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                self.pre = temp
            
            # Successor is the leftmost of right subtree
            if root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                self.suc = temp
            return

        # If key is less than root, go left and update successor
        elif key < root.data:
            self.suc = root
            self._helper(root.left, key)
        
        # If key is greater than root, go right and update predecessor
        else:
            self.pre = root
            self._helper(root.right, key)
