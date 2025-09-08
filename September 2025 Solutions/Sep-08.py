class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def mergeSort(self, head):
        # Base case
        if not head or not head.next:
            return head

        # Step 1: Find the middle
        middle = self.getMiddle(head)
        next_to_middle = middle.next
        middle.next = None

        # Step 2: Sort both halves
        left = self.mergeSort(head)
        right = self.mergeSort(next_to_middle)

        # Step 3: Merge sorted halves
        return self.sortedMerge(left, right)

    def getMiddle(self, head):
        if head is None:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
