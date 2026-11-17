"""
Every edge given has undirected edges 

Has NO CYCLES, and NO self.loop (two different vertices attached to it)

we want to return an edge that can be removed so that he resulting graph is a tree of n nodes


Graph Theory:

A Tree: 

- Connected
- No Cycles


Cycle detection problem! 


A tree must have an N - 1 edges, this is our goldent ticket to solve\


we will use the algorithm Union Find + Path Compression! 


"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        """
        IMPORTANT TO REMEMBER: 
        - Tree -> n - 1 edges 
        - Given Edges -> n edges, we need to remove 1 to remove the cycle 
        """
        # maintain the parent of every single node 
        num_edges = len(edges) # remember this will have given edges

        # remember that there should be n nodes
        parent = [node_i for node_i in range(num_edges + 1)]

        # intializing the sizes of each connected component, we
        rank = [1] * (num_edges + 1)

        def find(node): 
            # if the node just equals its own parent (meaning we are at the root)
            # then we can stop and return, but if it isn't we call recursivelu
            if node != parent[node]: 
                parent[node] = find(parent[node])

            return parent[node]

            


        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            # This is where the cycle is detected
            if parent1 == parent2: 
                return False

            if rank[parent1] > rank[parent2]: 
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else: 
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True 


        for node1, node2 in edges: 
            if not union(node1, node2): 
                return [node1, node2]
        