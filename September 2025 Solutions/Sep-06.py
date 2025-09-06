class Solution:
    def lengthOfLoop(self, head):
        if not head:
            return 0

        slow, fast = head, head

        # Detect loop using Floyd’s Cycle Detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Loop detected
                return self.countNodesInLoop(slow)

        return 0

    def countNodesInLoop(self, node):
        count = 1
        temp = node.next
        while temp != node:
            count += 1
            temp = temp.next
        return count
