"""
NOTE: 

- key = [0] and value = [1] passed through 
- values should be inserted as ListNodes


- We will use hashmap + doubly linked list to ensure anytime we use the get, we are accessing the node, thus it counts as "most recently used", thus we bring that all the way to the front of the key's linked list

right will be most recently used!


Basically hashmap


WE WILL REMOVE LEASR RECENTLY USED: (LEFT SIDE)

WE WILL KEEP THE MOST RECENTLY USED TO THE RIGHT SIDE
"""
class ListNode: 
    def __init__(self, key, value, next=None, prev= None):
        self.key = key 
        self.value = value 
        self.next = next
        self.prev = prev


# NOTE, if capacity is full

class LRUCache:
    def __init__(self, capacity: int): 
        self.capacity = capacity
        self.cache = {}
        
        # Making dummy nodes to the left and right to be easily accessible and replaceble 
        self.left, self.right = ListNode(0,0), ListNode(0,0)

        #Lets have them point at each other now 
        self.left.next = self.right 
        self.right.prev = self.left 
        
    
    def get(self, key: int): 
        if key in self.cache:
            # ensures we remove the least recently used node and place it at the beginning of our Cache
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            # lastly we need to returns the node's value 
            return self.cache[key].value
        
        # if failed/ doesn't exist
        return -1




    def put(self, key: int, value: int):
        # THERE IS AN EDGE CASE, key already exists but value is different! ( lets come up with something that handles both cases)
        if key in self.cache: 
            #lets remove the key and make a new one with the new value, else we'll skip removing it 
            self.remove(self.cache[key])
        
        #New Node with a value 
        new_node = ListNode(key, value)

        # inserting into the dictionary for bookkeeping 
        self.cache[key] = new_node 

        # NOW we insert into our LINKED LIST for LRU caching algorithm
        self.insert(self.cache[key])

        # What happens if we reached capacity?-> We need to remove the least recently used 
        if len(self.cache) > self.capacity: 
            least_recently_used = self.left.next
            self.remove(least_recently_used)

            # NOTE WE STILL NEED TO DELETE IT FROM OUR HASHMAP!!! 
            del self.cache[least_recently_used.key]


    # We always insert the most recent at the right of our doubly linked list
    def insert(self, node):
        last_node_before_right_dummy_node = self.right.prev 
        right_dummy_node_end = self.right 


        """
        insert 5

         4 -> right 
            <-
        
        """
        node.next = right_dummy_node_end
        node.prev = last_node_before_right_dummy_node

        right_dummy_node_end.prev = node 

        last_node_before_right_dummy_node.next = node 

    def remove(self, node): 
        # Just regularly removing a node from a doubly linked list 
        node_before_the_node_being_removed, the_node_after_the_node_being_removed = node.prev, node.next

        node_before_the_node_being_removed.next, the_node_after_the_node_being_removed.prev = the_node_after_the_node_being_removed, node_before_the_node_being_removed

        







       
        
        


        
