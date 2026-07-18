# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        # NOTE: an intersection means, both listNode are part of headA and HeadB path, 
        # Thus, we dont compare its value, we compare the actual list node itself 
        full_a_linked_list = set()
        # NOTE: in python a hashset doesn't only require numerical value but rather a custom object list Nodes can be hashed
        

        #so we need pointer for A
        current_pointer_A = headA

        # We can iterate through one of the pointer (1st pointer in this case A)
        while current_pointer_A: 
            # And we can add it to our hash set
            full_a_linked_list.add(current_pointer_A)

            # we must update the pointer again until we reach None listNode 
            current_pointer_A = current_pointer_A.next 



        #so we need pointer for B
        current_pointer_B = headB 

        #In this loop, we are now iterating until we find that the listNode in B's path is already in the hash set

        while current_pointer_B:
            if current_pointer_B in full_a_linked_list:
                return current_pointer_B
            
            current_pointer_B = current_pointer_B.next
        return None
        """

        #How can we make this better without using extra memory? 

        # We can use the length of both linked liosts, and match them (meaning is one is 6 and the other ios 5, have the one at 6 start earlier) 
        #so that we iteraye through both simultaneously? 


        """
        This is done through a very clever way. Check I pad for reference! 

        """
        # First step is intializing both currents
        curr_list1, curr_list2 = headA, headB
        
        # We want the loop to continue until we both pointers clash into each other 
        while curr_list1 != curr_list2:
            # This means they intersected! BUT IT ALSO COULD MEAN both have reached null, both lists reach null
            if curr_list1 is not None:
                curr_list1 = curr_list1.next
            else:
                curr_list1 = headB

            if curr_list2 is not None:
                curr_list2 = curr_list2.next
            else:
                curr_list2 = headA

        return curr_list1 
    """
    Think about why this works!

    If they are not connected at all either way they will eventually reach NONE and both will equal eachother }

    Think about it like this 

    5 + 6 = 11 and so does 6 + 5 = 11

    6 + 5
    5 + 6
    -------
    11  11.   This is why they at the second run be one the same wave length
    
    """



         





        