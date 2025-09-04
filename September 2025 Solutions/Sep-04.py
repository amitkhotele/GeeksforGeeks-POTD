class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        # Function to reverse a linked list from start to end
        def reverse(start, end):
            prev = None
            curr = start
            nxt = None
            while prev != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return end, start  # new head, new tail

        dummy = Node(0)
        dummy.next = head
        prev_group = dummy
        curr = head

        while curr:
            tail = curr
            count = 1

            # move tail pointer k-1 steps ahead
            while count < k and tail.next:
                tail = tail.next
                count += 1

            # if we have less than k nodes left, still reverse
            next_group = tail.next
            new_head, new_tail = reverse(curr, tail)

            # connect previous part with reversed group
            prev_group.next = new_head
            new_tail.next = next_group

            # move prev_group and curr to next group
            prev_group = new_tail
            curr = next_group

        return dummy.next
