"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#all we need to do is run bfs or dfs, and create node using class Node

class Node: 
    def __init__(self, val = 0, neighbors = None): 
        self.val = val 
        # empty array if no neighbor value is given
        if neighbors is not None: 
            self.neighbors = neighbors
        else: 
            self.neighbors = []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # HashMap that will map the old nodes given just a node and its neighbours
        oldToNewGraph = {}
        
        # Hashmap will allow us to return the start to our new node and store all the nodes
        def dfs(node): 
            # meaning we already came to an end and no other NEW nodes are left to be stored
            # Thus we can return out to the copy_node and append it
            if node in oldToNewGraph: 
                return oldToNewGraph[node]

            copy_node = Node(node.val)

            oldToNewGraph[node] = copy_node

            # basically we are going through the neighbours of the original node, and also make a copy of it's neighbours
            for nei in node.neighbors: 
                copy_node.neighbors.append(dfs(nei))
            return copy_node
        return dfs(node) if node else None

                



        