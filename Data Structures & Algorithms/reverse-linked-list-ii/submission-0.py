class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next
    
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        #creating an dummy Node that will be at the start of the list, this wille help us with upcoming edge cases!
        dummy_node = ListNode(0, head)

        left_previous_pointer, current_pointer = dummy_node, head

        #phase 1 of the algorithm just sets the left_pointer and curretn pointer up to match the "left"
        for index in range(left - 1):
            left_previous_pointer = current_pointer 
            current_pointer = current_pointer.next
        
        # Phase 2, we reverse from left to right 

        # we create a dummy reference for the first Node's pointer we are switcing!
        previous_for_reversed_node = None 

        # note the range should reflect the number of nubers from ex left = 2 and right = 4 whcih is 2,3,4
        for i in range (right - left + 1):
            temp_next = current_pointer.next
            current_pointer.next = previous_for_reversed_node

            # Here we are updating the previous to be the current 
            previous_for_reversed_node = current_pointer 

            # here we update the current pointer itself so that we iterate through linked list 
            current_pointer = temp_next

        # PHASE 3, cleaning up the left pointers and right pointers, cause rn 2 points to None and 5 (current Node) isn't linked to anything
        left_previous_pointer.next.next = current_pointer 
        left_previous_pointer.next = previous_for_reversed_node

        return dummy_node.next





        