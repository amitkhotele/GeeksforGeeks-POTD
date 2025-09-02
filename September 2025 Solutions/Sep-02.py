class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def swapKth(self, head, k):
        # Step 1: Count nodes
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        # Step 2: If k is greater than n, no swap
        if k > n:
            return head

        # Step 3: If kth node from start and end are same, no swap
        if 2 * k - 1 == n:
            return head

        # Step 4: Find kth node from beginning
        x_prev = None
        x = head
        for _ in range(1, k):
            x_prev = x
            x = x.next

        # Step 5: Find kth node from end (which is (n-k+1)th from beginning)
        y_prev = None
        y = head
        for _ in range(1, n - k + 1):
            y_prev = y
            y = y.next

        # Step 6: Swap previous pointers
        if x_prev:
            x_prev.next = y
        if y_prev:
            y_prev.next = x

        # Step 7: Swap next pointers
        temp = x.next
        x.next = y.next
        y.next = temp

        # Step 8: Update head if needed
        if k == 1:
            head = y
        if k == n:
            head = x

        return head
