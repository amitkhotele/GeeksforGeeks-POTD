class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head

        # Dummy nodes for 0, 1, and 2 lists
        zeroD = Node(-1)
        oneD = Node(-1)
        twoD = Node(-1)

        zero = zeroD
        one = oneD
        two = twoD

        # Traverse and connect nodes to respective lists
        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next

        # Connect the three lists
        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None

        # Updated head
        return zeroD.next
