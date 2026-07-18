
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0 

    
    def hash_function(self, key):
        return key % self.capacity
    
    #Again, just a reminder in which why we need to use nodes is because there is a chance 
    #we will collide after running this hash_function
    




    def insert(self, key: int, value: int) -> None:
        index_given_by_hash_function = self.hash_function(key)
        # BEFORE INSERTING, we need to check for the collision, so we need to use the head 
        # as our reference and check if that is None (cause that means no node has been added at that index)
        current_node = self.table[index_given_by_hash_function]

        if current_node is None:
            newListNode = ListNode(key, value)
            self.table[index_given_by_hash_function] = newListNode
            self.size+=1 

        else:
            # WE NEED a previous pointer!! Why? well cause in our loop we are only referring to current_node 
            # and current_node lowkey goes to None, which we can't use yk

            previous_node = None
            while current_node:
                # WAIT what else do we to do BEFORE inserting into an index??
                # Well BRO we cannot have any repeating keys IN THE SAME INDEX! this is an important check 
                # NOTE, that doesn't mean the value will be the same so we need to apply THAT change,
                # but again that doesn't require the key itself to change 

                # Lets lowkey think about why this makes sense: 
                # if I insert two values with key = 1 and different values, they really shouldn't be creating 
                # two different nodes for both keys, also the keys is what makes it easy to find the node 
                # we want to receive back
                if current_node.key == key:
                    current_node.value = value
                    return # this forces us to leave so the code below is ignored
                previous_node, current_node = current_node, current_node.next
            # if the key is NEW! Then we can create a fresh New List Node 
            newListNode = ListNode(key, value)
            previous_node.next = newListNode
            self.size += 1

            # NOTE each time we insert we should be checking our load factor = size(# of nodes) / capacity
        if self.size / self.capacity >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        index_given_by_hash_function = self.hash_function(key)
        current_node = self.table[index_given_by_hash_function]
       
        while current_node:
            if current_node.key == key:
                return current_node.value 
            current_node = current_node.next
        return -1



    def remove(self, key: int) -> bool:

        index_given_by_hash_function = self.hash_function(key)
        current_node = self.table[index_given_by_hash_function]

        previous_node = None #This will be needed later for when we actually delete the value, to update out linked list 

        while current_node:
            if current_node.key == key: 
                if previous_node:
                    previous_node.next = current_node.next

                # When would this be possible?? None -> head, well look at our code, this is only possible 
                # when we only have current_node in the linked list 
                else:
                    self.table[index_given_by_hash_function] = current_node.next

                self.size -=1 
                return True
            previous_node, current_node = current_node, current_node.next
        return False


    def getSize(self) -> int:

        return self.size #assuming we are keeping track of size each time we insert/remove!


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        # We are basically doubling the size of our hash, we just mulyiply the capacity by 2 
        # then create a new table, and insert the values in our old table to our new table
        new_capacity = self.capacity * 2 
        new_table = [None] * new_capacity

        #NOTE FOR RESIZING, old keys may be mapped to other places!!! why? well their mod values can map 
        # to other indexes, which would help spread the nodes and potentially make the retrieving time average constant time


        # How do we do this then?

        # lets go through each node in our array!
        for each_OG_node in self.table:
            while each_OG_node:
                #we need to reindex every node in each index of the array (note: it's possible that we have 
                #linked list of nodes at certain points of the array, hence the while loop)
                new_index_given_by_hash_index = each_OG_node.key % new_capacity

                # Now we create another inserting sort of logic that checks for collisions!
                if new_table[new_index_given_by_hash_index] is None:
                    new_table[new_index_given_by_hash_index] = ListNode(each_OG_node.key, each_OG_node.value)

                # else case is going to be a little more involved, this is when there already exists 
                # another node so # colision occurrs
                else:
                    current_node = new_table[new_index_given_by_hash_index]
                    while current_node.next:
                        current_node = current_node.next 

                    current_node.next = ListNode(each_OG_node.key, each_OG_node.value)
                each_OG_node = each_OG_node.next

        self.capacity = new_capacity 
        self.table = new_table


                        
                



