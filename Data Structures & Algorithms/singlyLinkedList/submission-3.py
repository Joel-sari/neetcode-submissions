

class ListNode:
    def __init__(self, val=0,next_node=None):
        self.val = val
        self.next_node = next_node


class LinkedList:
    
    def __init__(self):

        # We need to keep track of the head and the tail 
        self.head = ListNode(0) # this will be the dummy node that will help us keep

        # Note: Our tail will always be initialized where our head is also at (cause intially we just have one dummy node)
        self.tail = self.head

    # This method receives an index and iterates through the linked list to get that value 
    def get(self, index: int) -> int:
        # Remember! we created a dummy node, so we need the NEXT ONE (kinda like ignoring the first node)
        current_pointer = self.head.next_node
        # We start at index 0 !!
        index_count = 0

        # NOTE: this also handles if our list is empty since our current_pointer would just be None
        while current_pointer:
            # we first want to check if we at the right index every single time, this should come first!
            if index_count == index: 
                return current_pointer.val
            
            # We increment our i pointer each time 
            index_count += 1

            # Update our current_pointer
            current_pointer = current_pointer.next_node


        return -1 # we just return -1 because we didn't find a node with that index(we probably passed an index to big)! 
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        # NOW because of the dummy_node we can EASILY enter our insertHead!

        # We are inserting in front of head and behind the current first node

        # We use the dummy node's next value and apply it to our newly created node 
        new_node.next_node = self.head.next_node

        # then pointing the dummy nodes next to the new value inserted
        self.head.next_node = new_node 

        # NOTE! There is one edge case here! and that is SOLEY when we add to an empty listNode 

        # Real quick why only when the listnode is empty? Well think about it, when we add to the head, our tail 
        # doesn't change so there is no need to update it, we only need to update tail if it is 
        # the first value in list we are adding since we initalized it to point to the dummy node 

        # if the new_node is potining to None, then we know this is the first 
        # value we are inserting
        if new_node.next_node is None:
            # here we are updating the tail to not point to the dummy node anymore, it should point to the newly inserted node 
            self.tail = new_node 
            # Something to note, is if we were to add another node, tail will just remain in the previously isnerted node , which is correct! 

    def insertTail(self, val: int) -> None:
        #Two cases, one is just the regular insertion, else we also have an edge case 
        #if we have nothing in our list, but you'll notice this works for both! 
        self.tail.next_node = ListNode(val) # creating a ListNode using our tail pointer!!, Note: our tail will just point to None initially but now we just plug our new node in it's place
        # Now we need to update our tail attribute to be the new Node we inserted at the tail 
        self.tail = self.tail.next_node

        
        

    # This is taking into account that the first value is at index 0 
    def remove(self, index: int) -> bool:
        index_counter = 0 
        # We need current_pointer to be start at the dummy_node because when we remove a ndoe 
        # we need to reference the node below 
        current_pointer = self.head
        # we want index_counter to be less than index AGAIN to reference the node before it 
        #for removal! We also ensure we don't go outside of bound by checking current_pointer
        while index_counter < index and current_pointer:
            # Moves our node before our target node!
            index_counter += 1 
            current_pointer = current_pointer.next_node

        # At this point current_pointer.next_node is the target
        if current_pointer and current_pointer.next_node: 

            # we need an edge case in which we check if our target of removal is the tail, then we need to update the tail!
            if current_pointer.next_node == self.tail:
                self.tail = current_pointer




            # we are removing the one in between current_pointer and current_pointer.next_node.next_node
            current_pointer.next_node = current_pointer.next_node.next_node
            # we can actually remove it, thus return true
            return True 
        #else we return false cause we cannot remove anything 
        return False

    def getValues(self) -> List[int]:

        current_pointer = self.head.next_node
        array_of_list_nodes = []
        while current_pointer:
            # We are appending the list (cause we can't append the actual objects)
            array_of_list_nodes.append(current_pointer.val)
            current_pointer = current_pointer.next_node

        return array_of_list_nodes
        
