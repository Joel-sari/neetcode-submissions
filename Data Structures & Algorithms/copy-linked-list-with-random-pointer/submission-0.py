
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldNodeToNewNode = {None: None}

        current_pointer = head 

        while current_pointer: 
            create_copy = Node(current_pointer.val)

            # This maps the actual node given by head and creates a link to the copy
            oldNodeToNewNode[current_pointer] = create_copy
            current_pointer = current_pointer.next
        
        second_current = head
        while second_current:
            copy = oldNodeToNewNode[second_current]
            copy.next = oldNodeToNewNode[second_current.next]
            copy.random = oldNodeToNewNode[second_current.random]
            second_current = second_current.next

        return oldNodeToNewNode[head]

        