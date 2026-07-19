# This is the normal solution
class DoubleListNode:
    # This is our doubl
    def __init__(self, val= 0, next = None, prev = None ):
        self.val = val
        self.next = next
        self.prev = prev
        

class MyLinkedList:

    # First we need to create a head and tail for our double linked list
    # here we can create a dummy listNode to indicate the end and start
    # to a double linked list
    def __init__(self):
        self.head = DoubleListNode(-1)
        self.tail = DoubleListNode(-1)
        self.head.next = self.tail 
        self.tail.prev = self.head 

    def get(self, index: int) -> int:

        if index < 0:
            return -1

        current_node = self.head.next
        count_of_nodes = index 

        # Since we are using dummy nodes, we will count our tail node as our stopping point
        while current_node != self.tail  and count_of_nodes > 0:
            current_node = current_node.next
            count_of_nodes -= 1 

        if current_node == self.tail: 
            return -1

        return current_node.val

    def addAtHead(self, val: int) -> None:

        # first we make a new node
        new_node = DoubleListNode(val)

        # the update it's next and previous values to make sense 
        new_node.next = self.head.next 
        new_node.prev = self.head

        # we still need to update the current "top" node's previous attribute
        self.head.next.prev = new_node

        #and then we need to update our dummy head to point to the new_node! 
        self.head.next = new_node 


        

    def addAtTail(self, val: int) -> None:
        new_node = DoubleListNode(val, self.tail, self.tail.prev)
        self.tail.prev.next = new_node 
        self.tail.prev = new_node 
        
        
        

    def addAtIndex(self, index: int, val: int) -> None:

        # Check if the index input is even valid 
        if index < 0: 
            return
        successor_node = self.head.next 
        count_of_nodes = index

        while successor_node != self.tail and count_of_nodes > 0:
            successor_node = successor_node.next 
            count_of_nodes -= 1
        
        # this is indicates we are out of bounds
        if count_of_nodes > 0 and successor_node:
            return 
        else:
            new_node = DoubleListNode(val)
            predecessor_node = successor_node.prev

            predecessor_node.next = new_node
            successor_node.prev = new_node 
            new_node.next  = successor_node
            new_node.prev = predecessor_node

                 

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return 

        current_node = self.head.next
        count_of_nodes = index
        while current_node != self.tail and count_of_nodes != 0:
            current_node = current_node.next
            count_of_nodes -= 1

        if current_node == self.tail:
            return 
        current_node.prev.next = current_node.next 
        current_node.next.prev = current_node.prev
        

        

         

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)