# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)

        prev_k_group_start_node = dummy_node 

        while True:

            last_node_in_prev_k_group = self.getKth(prev_k_group_start_node, k)

            # if we reach out of bounds, then we can exit out the while loop
            if not last_node_in_prev_k_group: 
                break

            next_k_group_node = last_node_in_prev_k_group.next

            # So now lets go ahead and do reversion 
            # dummy -> 1 -> 2 -> 3 -> 4 -> 5, picture     3,           1
            previous, current = last_node_in_prev_k_group.next, prev_k_group_start_node.next

            while current != next_k_group_node: 
                temporary = current.next # this would 1 -> 2
                current.next = previous # 1-> 3 

                # updating our pointers
                previous = current # 3 changes to 1 
                current = temporary # now this is 2

            temp_first_node_in_group = prev_k_group_start_node.next # 1 -> 3 3 (is .next) 3 = temp
            prev_k_group_start_node.next = last_node_in_prev_k_group #  0 -> 2 
            prev_k_group_start_node = temp_first_node_in_group

        return dummy_node.next
        




    def getKth(self, current_node, k): 
        while current_node and k > 0: 
            current_node = current_node.next 
            k -=1 
        return current_node
        