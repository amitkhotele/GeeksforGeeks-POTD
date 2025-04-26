'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Your Function Should return True/False
    def isHeap(self, root):
        # Function to count number of nodes
        def countNodes(node):
            if not node:
                return 0
            return 1 + countNodes(node.left) + countNodes(node.right)
        
        # Function to check completeness
        def isComplete(node, index, total_nodes):
            if not node:
                return True
            if index >= total_nodes:
                return False
            return (isComplete(node.left, 2 * index + 1, total_nodes) and
                    isComplete(node.right, 2 * index + 2, total_nodes))
        
        # Function to check Max-Heap property
        def isMaxHeap(node):
            if not node:
                return True
            
            # Leaf node
            if not node.left and not node.right:
                return True
            
            if node.left and not node.right:
                return node.data >= node.left.data and isMaxHeap(node.left)
            
            if node.left and node.right:
                return (node.data >= node.left.data and
                        node.data >= node.right.data and
                        isMaxHeap(node.left) and
                        isMaxHeap(node.right))
            
            return False  # This condition shouldn't happen in a complete tree
        
        total_nodes = countNodes(root)
        return isComplete(root, 0, total_nodes) and isMaxHeap(root)
