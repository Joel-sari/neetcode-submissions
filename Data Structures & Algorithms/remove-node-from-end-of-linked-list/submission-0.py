# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
okay so the way to solve this problem is actially by using a left and right pointer. Now the way to do it is
actually very genius. Since yk linked lists aren't arrays ( we can't just use the index)
we can use pointers. Okay but how does that help, well since it's the nth last node in the linkedlist

lets identify that space! By setting the right pointer to have a space of n from the left pointer, we
set up this difference as long as we update both pointers until right_pointer hits null and left hits 
the node we want. it is very genius 

Now we also have to delete it ! need that nth node, how? well we could use a dummy node!!!, why this is good?
well again we need to delete the nth node, but if out pointer is on the nth node, it's incoveneient, 
we instead want to be on the node before it to update that nodes pointer to be 5 instead of 4 in a 

dummy -> 1 -> 2 -> 3 -> 4 -> 5


We couldve also just reversed the list too 


"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        left_pointer = dummy

        right_pointer = head


        # This shifts the pointer n times by causing a loop of .next 
        while n > 0 and right_pointer: 
            right_pointer = right_pointer.next
            n -=1

        # While right_pointer still exists
        while right_pointer:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next

        # Like if it is 1 -> 2 -> 3 -> 4 , and we are tryna remove 3, then 2 next points to 4 instead of 3
        left_pointer.next = left_pointer.next.next

        
        return dummy.next



        



      



        