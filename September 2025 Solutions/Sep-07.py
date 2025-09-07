import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def mergeKLists(self, arr):
        # Min-heap for (node value, index, node)
        heap = []
        
        for idx, head in enumerate(arr):
            if head:  # push only non-empty lists
                heapq.heappush(heap, (head.data, idx, head))
        
        dummy = Node(0)
        tail = dummy
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            
            # attach the smallest node to merged list
            tail.next = node
            tail = tail.next
            
            # if next node exists, push it into heap
            if node.next:
                heapq.heappush(heap, (node.next.data, idx, node.next))
        
        return dummy.next
