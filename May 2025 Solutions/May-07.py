class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def Paths(self, root):
        all_paths = []
        
        def dfs(node, path):
            if not node:
                return
            path.append(node.data)
            
            if not node.left and not node.right:
                # Leaf node reached, store the path
                all_paths.append(path[:])
            else:
                # Continue exploring left and right
                dfs(node.left, path)
                dfs(node.right, path)
                
            # Backtrack
            path.pop()
        
        dfs(root, [])
        return all_paths
