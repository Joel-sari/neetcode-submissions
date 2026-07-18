"""
The way we go about creating the Deque structure is using List Nodes 
to create a doubly linked list, we should keeo track of the head and tail !

and our Node should have a next and previous pointer to help us get rid of the tail!


We will do this by intiializing a dummy head and dummy tail node, this will allow us to 
reference both objects we create quickr and more efficiently

"""

class ListNode: 
    def __init__(self, value):
        self.value = value 
        self.next_node = None 
        self.previous_node = None

        
class Deque:
    

    def __init__(self):
        # Both dummy Nodes
        self.head  = ListNode(0)
        self.tail = ListNode(0)

        # Now we want to connect both the head and tail! so theypoint like this:
        # dummy_head -> dummy_tail 
        # dummy_head <- dummy_tail 
        self.head.next_node = self.tail
        self.tail.previous_node = self.head
        

        
    def isEmpty(self) -> bool:
        # NOTE: we use dummy nodes, so we can't just say they if they dont exist 
        # rather we need to say if there is no node in between 
        return self.head.next_node == self.tail
        
        

    # Appending occurs at the end of the Queue
    def append(self, value: int) -> None:
        new_node = ListNode(value)

        #Why not the self.tail itself??? Well cause remmeber our tail and
        # head are dummy nodes!! so we need the one before!
        current_last_node = self.tail.previous_node

        # Now we need to just manipulate the pointers! 
        current_last_node.next_node = new_node
        new_node.previous_node = current_last_node
        new_node.next_node = self.tail
        # lastly we need to update the previous pointing node of tail
        self.tail.previous_node = new_node




    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)

        # This points to the first node rather than the dummy node.
        current_first_node = self.head.next_node

        # Now we ned to update the new nodes connections
        current_first_node.previous_node = new_node
        new_node.previous_node = self.head
        new_node.next_node = current_first_node

        # lastly we need to update and ensure head points to our newly inserted value 
        self.head.next_node = new_node
        
        


        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        # else we can remove the last node 
        last_node_being_deleted = self.tail.previous_node
        # We need to store the value somewhere, so we can return it
        value = last_node_being_deleted.value

        node_before_the_one_being_deleted = last_node_being_deleted.previous_node


        node_before_the_one_being_deleted.next_node = self.tail
        self.tail.previous_node = node_before_the_one_being_deleted

        return value


    def popleft(self) -> int:
        if self.isEmpty():
            return - 1
        first_node_being_deleted = self.head.next_node
        
        value = first_node_being_deleted.value

        # this is gonna be the next "first" node after we delete the current first_node
        node_after_the_one_being_deleted = first_node_being_deleted.next_node


        # update pointers that remove the pointers 
        node_after_the_one_being_deleted.previous_node = self.head
        self.head.next_node = node_after_the_one_being_deleted
        return value 

