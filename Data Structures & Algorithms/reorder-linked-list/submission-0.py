# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

"""
The whole purpose is to reorder the linked list from okay lets say we have two pointers
one at the end of the list and the othef at the beginning, we add start with beginning and then end and then begginging and end 
each time incrementing / decrementing the pointers till we end up stopping

Note we dont return anything, just modify the list

"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # We are creating two pointers using rabbit and tortoise to figure out the halfway point
        # of the linkedlist 
        slow_turtle = head 
        fast_rabbit = head.next 

        # we go until fast_rabbit reaches the finish line, and turtlw will be half way
        while fast_rabbit and fast_rabbit.next:
            slow_turtle = slow_turtle.next
            fast_rabbit = fast_rabbit.next.next

        #This is the starting point for the second half of the linked list.
        second_half_of_list_starting_point = slow_turtle.next 

        #Now we are setting our last next value in the first half of the linked list to null
        slow_turtle.next = None

        # this will serve as the null end of the linked list
        previous = None

    


        #Now lets reverse the second half of the list
        while second_half_of_list_starting_point:
            # if we had 3 -> 4, 4 would be held in the temp valiue
            temporary_for_second_list = second_half_of_list_starting_point.next

            #3 will now point to None instead of 4, so 3 --> None     4 = temp
            # crucail step as it destroys the current next and uses the previous value instead
            second_half_of_list_starting_point.next = previous


            #previous will now equal the starting point the node we just edited 
            previous = second_half_of_list_starting_point 

            #And now we update the pointer to go to the disconnected part of the list we stored
            second_half_of_list_starting_point = temporary_for_second_list
        
        # merging two halfs, note after our while loop above, we need to point to its begining value
        # which would be the previous (which stores like the last value before none)


        #gathering our two pointers that we will use in our while loop
        second_half_of_list_starting_point = previous
        first_half_of_list_starting_point = head

        while second_half_of_list_starting_point:

            #storing our next node to not lose them
            temp1, temp2 = first_half_of_list_starting_point.next, second_half_of_list_starting_point.next

            #first halfs starting node will pointt to the first node on the second list
            first_half_of_list_starting_point.next = second_half_of_list_starting_point

            # then we are making sure that the second_half pointer that lowkey got inserted as the second value (first values .next)
            # we use the intial first half_of_list .next equal to the second halfs .next value.
            second_half_of_list_starting_point.next = temp1

            # Think of the above as combining three elements at the same time, the already 
            # sorted linked list we have, the second list and then the next on the first stored


            # Now we have to update the pointers, why temp? well temp is lowkey our moving pointer
            # since it's the next items on the list 
            first_half_of_list_starting_point, second_half_of_list_starting_point = temp1, temp2







        


        