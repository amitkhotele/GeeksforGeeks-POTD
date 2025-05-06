class Solution:
    def LeftView(self, root):
        if not root:
            return []
        
        from collections import deque
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # The first node of the current level
                if i == 0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
