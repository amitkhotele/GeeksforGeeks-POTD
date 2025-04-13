class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution():
    def cloneGraph(self, node):
        if not node:
            return None

        # Dictionary to save the cloned nodes
        old_to_new = {}

        def dfs(curr_node):
            if curr_node in old_to_new:
                return old_to_new[curr_node]

            # Clone the node
            copy = Node(curr_node.val)
            old_to_new[curr_node] = copy

            # Clone all the neighbors
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
