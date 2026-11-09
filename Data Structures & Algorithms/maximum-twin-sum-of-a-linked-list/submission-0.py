# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
We are basically pairing up the following nodes 

 node 1 ->  node 2 ->   node 3 ->   node 4
 pair 1     pair2       pair 2      pair 1


 we could have 

 node 1 ->  node 2 ->   node 3 ->   node 4 -> node 5
 pair 1     pair2        pair3      pair 2      pair 1



There are a few ways to solve this but the main hurdle is the idea that the linked list is a one way face data structure 

so two pointers would usually be the approach, starting from the ends and making our way to the inside, this would need to use an array data structure

but what if we wanted to maintain our linked list data structure? 

we could iterate half way through the linked list: 
    once we iterate half way through we would go from the inner middle to the outer ends
    - as we iterate to the middle, we must ensure we change the connections .nextes) to face in reverse order!
    - that way we can go from inner to outer

    - to get to the middle we will use slow and fast pointers! 


NOTE: The linked list will always be of positive length 


"""
class ListNode: 
    def __init__(self, val = 0, next = None): 
        self.val = val 
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # both slow and fast pointers
        slow_right, fast_boundary_ptr = head, head

        previous_left = None

        # we need to check the next two spots before reaching the end of the linked list
        while fast_boundary_ptr and fast_boundary_ptr.next: # fast either last point or out of bounds

            fast_boundary_ptr = fast_boundary_ptr.next.next
            #we need to rearrange the pointers to create the link backwards
            next_slow_temp = slow_right.next
            slow_right.next = previous_left
            previous_left = slow_right
            slow_right = next_slow_temp


        result_sum = 0 

        # note: we only care about side's bounds since both sides will be divided equally.
        while slow_right: 
            # also note that slow will be in front by one, thus our left side will start with pr
            result_sum = max(result_sum, previous_left.val + slow_right.val)
            previous_left = previous_left.next 
            slow_right = slow_right.next

        return result_sum


        

        