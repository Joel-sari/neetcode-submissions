# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        My algorithm approach: Is to use to pointers/currents, one in which 
        goes at 2x the speed and the other goes half the speed. 
        
        """
        slow_pointer = head 
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer


        