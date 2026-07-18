# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """
        This is basically for values!! (my own intuition) we need to keep track of the NODES!
        hashy = {}

        while head:
            hashy[head.val] = hashy.get(head.val, 0) + 1
            if hashy[head.val] > 1:
                return True
            head = head.next

        return False
        """

        # The hash set way, using spacecomplexity of O(n)

        """
        visited = set()
        current = head

        while current:
            if current in visited: 
                return True
            
            visited.add(current)
            current = current.next 

        return False
        """

        turtle = head
        rabbit = head 

        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                return True

        return False




        