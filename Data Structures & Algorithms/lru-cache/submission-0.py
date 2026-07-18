class ListNode: 
    def __init__(self, key, val):
        self.val = val 
        self.key = key 
        self.next = None 
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {} # this will map the key into the nodes 

        # We need a DUMMY RIGHT AND LEFT POINTER 

        # left will be least recent used, and right is the most recent 
        self.left, self.right = ListNode(0,0), ListNode(0,0)

        # Note the outer "nodes". meaning left.prev and right.next at these dummy nodes are NON EXISTSNET 
        # SINCE THESE DUMMY NODES REPRESENT THE EDGE of our doubly linked list! 
        self.left.next, self.right.prev = self.right, self.left 
        # And again intitially these will point at eachother!

    def get(self, key: int) -> int:
        if key in self.cache: 

            #To update recent and least recent! we can use our own built in functions to remove the least and move up to the front of the cache!
            # again our goal is to keep track of like the last time it was used using our dummy nodes and internal functions
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # REMEMEBER cache[KEY] gives us the Node, thus we need to use .val  to get the actual value 
            return self.cache[key].val 
        #We return -1, we fail!
        return -1
        

    def put(self, key: int, value: int) -> None:
        # One edge case, if we are tryna insert at a key that already exists! then we need to update rather thanadd a new one 
        if key in self.cache:
            # we initially remove from out list so we can just honestly create a new node!
            self.remove(self.cache[key])

        # Again creating a node and putting it in the hashmap 
        self.cache[key] = ListNode(key, value)
        # We also need to insert into our list that keeps track of recents
        self.insert(self.cache[key])


        # If we have reached capacity, then we remove the least recent! and delete from the hash! 
        # How do we remove the least recently used, or how do we even know where its at? 
        # LEFT.NEXT!!!!
        if len(self.cache) > self.capacity:

            # This is our LRU 
            least_recently_used = self.left.next

            # We then want to remove it from our cache 
            self.remove(least_recently_used)

            # AND NOW we can use the del function to remove the hash value, using the .key lets us reference the key to delete it from our hash 
            del self.cache[least_recently_used.key]




    

    #Helper functions REMOVE AND INSERT 

    #removes from left (least recently used)
    def remove(self, node):
        # The node that is being passed in as a argument is middle node we are tryting to get rid of
        prev_middle_node, next_middle_node = node.prev, node.next 
        prev_middle_node.next, next_middle_node.prev = next_middle_node,  prev_middle_node


    # adds to the right, (most recently used) this is where we move our new values or getting 
    def insert(self, node):
        # Notice the next is just self.right because self.right is at the furthest right end
        prev, next = self.right.prev, self.right 
        prev.next = node 
        next.prev = node
        node.prev = prev
        node.next = next

        
