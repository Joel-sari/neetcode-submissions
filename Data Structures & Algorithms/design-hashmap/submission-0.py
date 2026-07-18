"""
We will use an array to map out the ellemnts in hashmap 

key = index
value = element 

We will mod by 1000, if we reach a number over 1000, then they will be mapped from 1-1000 without going far away 

collisions:
what if we have mulitple values that fall at the same key 

We will tackle collisions with chaining, in a linked list manner 

Ex:
we are given 
100, 1
1100, 2

we would have 

key = 100 , Nodes: 100,1 -> 1100, 2


We need to use a dummy node for each linked list so that we don't get rid of the head that is attached tp the key 
"""
class ListNode:
    def __init__(self, key= -1, val = -1, next=None):
        self.key = key 
        self.val = val 
        self.next = next 
    

class MyHashMap:
    def __init__(self):

        # We are going to create an array with each index having a dummy listNode
        self.map = [ListNode() for i in range(1000)]
        #at this point each index in the array of 1000 has one Empty List Node 
        
    def mapping(self, given_key: int):
        # This figures out where the actual index key is in our 1000 key "dictionary" (its an array)
        index_key = given_key % len(self.map)
        return index_key # crucial so we find out where to place a new node!

    def put(self, key: int, value: int) -> None:
    
        # Once we figure out (using .mapping) where the correct indec is we pass in the ListNode at that index into 
        # current_list_node, gives us the DUMMY Node at that array index
        current_list_node = self.map[self.mapping(key)]

        # We will continue to traverse down the linked list in the index given that current_list_node is not None
        # Notice intially we start with an empty Linked List (THIS iS THE DUMMY NODE) and it's next is None, so we pretty much skip it 
        while current_list_node.next:

            # if for example our key was 9 and val was 2, but earlier we did key: 9 and val 1 
            # then we have to update the new value! cause put is not only tryna add new values 
            # but modify existing ones. NOTE:  WE EXPLICTLY CHECK THE KEYS AS THOSE AREN"T PUT THROUGH THE MAPPING FUNCTION, so the 
            #user truly is updating †he value at that key
            if current_list_node.next.key == key: 
                # This is again basically just the user tryna update the value 
                current_list_node.next.val = value 
                return 

            #Update to the next List Node (if it even exists, cause if not it becoems None)
            current_list_node = current_list_node.next 
        
        # If we never find the key OR we have only an dummy node, meaning its a WHOLE NEW KEY ex: key 1 = 9 and key 2 = 1009
        # Then we must create a new List Node and update the dummy nodes' or the last node in the linked lists .next to be equal to a new list node value  
        current_list_node.next = ListNode(key, value)
        
        

    def get(self, key: int) -> int:
        # To get the value, we would just need to 1. Map  it corectly with the key given 
        #2. we need to iterate through linked list to find it

        
        #1. first finding where in the array and initializing out starting point at the dummy node 
        current_list_node = self.map[self.mapping(key)] 

        # Again we start with the next element since we don't have to check the dummy node 
        while current_list_node.next:
            if current_list_node.next.key == key: 
                return current_list_node.next.val

            current_list_node = current_list_node.next
        return -1

    def remove(self, key: int) -> None:
        
        # Again we are locating the index in the array and starting at the dummy node 
        current_list_node = self.map[self.mapping(key)]
        #NOTE: we want TO ENSURE WE ARE NOT DELETING THE DUMMY NODE: 
        # How can we do that? well we check to see if both current and current.next are None, if curr.next is none and current isn't
        # Then we know that is a dummy node, and we CANNOT remove it! 
        while current_list_node and current_list_node.next: 
            if current_list_node.next.key == key: 
                
                # This "deletes" the node by updating the current pointer that was on next, to next's next.
                current_list_node.next = current_list_node.next.next
                return 
            current_list_node = current_list_node.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)