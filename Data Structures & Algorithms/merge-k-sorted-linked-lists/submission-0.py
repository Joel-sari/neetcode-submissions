# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Handling edge cases
        if not lists or len(lists) == 0:
            return None
         
        # Taking pairs of linked Lists and merging them each time 
        while len(lists) > 1: 
            mergedLists = []
            
            # This is the main part of when we are seperating them
            for index in range(0, len(lists), 2):
                list_1 = lists[index]
                # Note: there is a chance we may go out of bounds, so check before applying it to list_2. If not, we can just have an empty list, thats okay too
                list_2 = lists[index + 1] if index + 1 < len(lists) else None

                mergedLists.append(self.mergeList(list_1, list_2))

            lists = mergedLists
        return lists[0]
        

    
    # Merging both lists, it's easy when using a dummy node 
    def mergeList(self, list_1, list_2):

        # This is like the start to a combined linked list
        dummy_node = ListNode()

        # will use this as a pointer ( kinda like k in merge sort)
        pointer = dummy_node

        while list_1 and list_2:
            if list_1.val <= list_2.val: 
                # start points to list_1
                pointer.next = list_1
                list_1 = list_1.next 
            else: 
                pointer.next = list_2
                list_2 = list_2.next
            # updating the pointer to welcome the next upcoming node
            pointer = pointer.next  

            # then there is a chance that either end still exists
        if list_1: 
            pointer.next = list_1
        if list_2: 
            pointer.next = list_2

        return dummy_node.next 







        