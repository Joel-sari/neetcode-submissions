# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
Given non empty linked lists, so we can assume they always have a value

non negative integers only -> so there can't be negative integers

Digits are stored in reversed order! (actually helps us!)


A case to consider:
lets take  465 + 3342, notice they have different number of digits, meaning one linked list has a smaller node
            (carry of +1)
5   ->   6   ->   4  
2   ->   4   ->   3   ->   3

7.  ->   0   ->   8   ->   3

"""
class ListNode: 
    def __init__(self, val = 0, next = None):

        self.val = val

        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        #Creating a dummy node that will serve as the head to our merged linked List
        #NOTE: it makes life so much more easier!! makes mergging easier
        dummy = ListNode()
        current_pointer = dummy

        # this will hold the carry value 
        carry = 0

        # we will need to iterate until either list is null 

        # remember there is a chance that we have null + null + 1 so we also need to take into acount the carry 
        while l1 or l2 or (carry > 0) : 

            # we are setting a value variable to reference l1.val ELSE if l1 is null then it should just be 0
            value1 = l1.val if l1 else 0

            # we are setting a value variable to reference l2.val ELSE if l1 is null then it should just be 0
            value2 = l2.val if l2 else 0


            #total value / new digit 
            total_value = value1 + value2 + carry

            # lets say we got 15, well the carry will be tots_value/15 = 1
            carry = total_value// 10
            

            # lets say we got 15, the digit we wanna keep must be SINGULAR, in this case 5
            total_val = total_value % 10


            # Inserting a new list node to our initialized linked list
            # the whole point is just us creating a newly formed linked list
            current_pointer.next = ListNode(total_val)

            #updating our pointers!
            current_pointer = current_pointer.next

            # for our individual lists we are updating their pointer too if it exists else we just keep it None (which will just convert itslef into 0 like we did in the beginning)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        