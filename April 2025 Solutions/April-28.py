# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getMaxSum(self, root):
        def solve(node):
            if not node:
                return (0, 0)  # (incl, excl)
            
            left_incl, left_excl = solve(node.left)
            right_incl, right_excl = solve(node.right)
            
            # If we include current node, we can't include children
            incl = node.data + left_excl + right_excl
            
            # If we exclude current node, we can choose max from children (incl/excl)
            excl = max(left_incl, left_excl) + max(right_incl, right_excl)
            
            return (incl, excl)
        
        incl, excl = solve(root)
        return max(incl, excl)

