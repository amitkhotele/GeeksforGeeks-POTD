class Solution:
    def reverse(self, head):
        current = head
        temp = None
        
        while current is not None:
            temp = current.prev  # Store prev pointer
            current.prev = current.next  # Swap next and prev
            current.next = temp
            
            # Move to the next node in the original list
            # The next node is now pointed to by the previous pointer
            current = current.prev
        
        # After the loop, the head of the reversed list
        # is the last non-null value of 'temp'
        if temp is not None:
            head = temp.prev
        
        return head
