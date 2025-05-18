from collections import deque

class Solution:
    def findSpiral(self, root):
        if not root:
            return []
        
        result = []
        dq = deque()
        dq.append(root)
        
        left_to_right = False  # False -> right to left (even levels)
        
        while dq:
            level_size = len(dq)
            level_nodes = []
            
            for _ in range(level_size):
                node = dq.popleft()
                level_nodes.append(node.data)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            # Reverse the level nodes depending on direction
            if left_to_right:
                result.extend(level_nodes)
            else:
                result.extend(level_nodes[::-1])
            
            # Flip direction for next level
            left_to_right = not left_to_right
        
        return result
