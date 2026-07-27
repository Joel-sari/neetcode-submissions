class ListNode: 
    def __init__(self, value: int, next=None, prev=None):
        self.next = next 
        self.prev = prev
        self.value = value
        

class Deque:
    
    def __init__(self):
        # Lets make some dummy nodes for the tail and head 
        self.head = ListNode(0)
        self.tail = ListNode(0)

        self.head.next = self.tail 
        self.tail.prev = self.head 

    def isEmpty(self) -> bool:
        if self.head.next == self.tail and self.tail.prev == self.head: 
            return True 
        return False
        
        
    def append(self, value: int) -> None:
        
        last_node = self.tail.prev
        new_node = ListNode(value)
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node
        
    def appendleft(self, value: int) -> None:

        first_node = self.head.next
        new_node = ListNode(value)
        first_node.prev = new_node
        new_node.next = first_node
        new_node.prev = self.head
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty(): 
            return -1 
        else:
            current_node = self.tail.prev 

            # we need to retun the node being popped
            value_returned = current_node.value
            new_last_node = current_node.prev


            new_last_node.next = self.tail 
            self.tail.prev = new_last_node

        return value_returned
        
        

    def popleft(self) -> int:
        if self.isEmpty(): 
            return -1 
        else: 
            current_first_node = self.head.next

            value_returned = current_first_node.value

            new_first_node = current_first_node.next 

            new_first_node.prev = self.head 
            self.head.next = new_first_node
            return value_returned

        
