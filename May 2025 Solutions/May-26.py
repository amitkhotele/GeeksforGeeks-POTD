class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case 1: Empty list
        if head is None:
            new_node.next = new_node
            return new_node

        curr = head

        while True:
            # Case 2: Insert in normal sorted order
            if curr.data <= data <= curr.next.data:
                break

            # Case 3: Insert at the turning point (end to start)
            if curr.data > curr.next.data:
                if data >= curr.data or data <= curr.next.data:
                    break

            curr = curr.next

            # Case 4: Full loop, insert anywhere
            if curr == head:
                break

        # Insertion
        new_node.next = curr.next
        curr.next = new_node

        # Ensure the head remains the smallest
        return head if head.data <= data else new_node
