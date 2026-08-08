
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_pointer = head
        previous = None
        while current_pointer is not None: 
            """
            Example 1 -> 2 -> 3 -> 4

            first iteration: 
            previous: None 
            temp_var -> 2 
            1 now points to None (as it should since it is the tail)

            # now we just need to move up the linked List

            current_pointer is now at 2 ( get it from the temp variable)
            previous is at 1 

            
            """
            temp_var = current_pointer.next
            current_pointer.next = previous
            previous = current_pointer
            current_pointer = temp_var


        return previous
        