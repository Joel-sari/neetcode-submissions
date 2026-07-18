"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



"""

"""
Example : 1 ------- 2
          |         |
          |         |
          4 ------- 3

hashMap = { 1og : 1c  }

"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #Quick note AGAIN notice, the hashmap regardless of the recursion
        #will always hold the updates, just imprtant to know in case wanted to delete 
        # a key and value in our hashmap!
        hash_old_to_new = {}

        def dfs(node):
            # kinda of our base case, but saying if we already have our node noted down in our hashmap
            # If it's "cloned already"
            if node in hash_old_to_new:
                return hash_old_to_new[node]

            
            # when we initially create the clone of this node, we essentially are 
            #only passing in the node.val for value, not it's neighbors which means 
            #that intially will just be an empty array []. This is done purposefully 
            #as we will see how it will change on our recursive steps
            creating_clone = Node(node.val)
            
            #NOTE: we arte using NOTE OBJECTS to in our hashmap, i jsut find it pretty cool
            #that objects can serve as keys and as values!
            hash_old_to_new[node] = creating_clone


            #Now we must account for the neighbors the clone may have.
            #Notice we use the og node's neighbors as our range. AGAIN THIS iS POSSIBLE 
            # BECAUSE THE CLONE IS AN OBJECT, so it can store.neighbors!!

            #Furthermore, we then recursively call dfs and appending it to our copy 
            for neighbor in node.neighbors:
                creating_clone.neighbors.append(dfs(neighbor))
            return creating_clone
        if node:
            return dfs(node)
        else:
             return None


        