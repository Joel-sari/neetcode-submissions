"""
A tree must have the following: 

-  All Nodes Must Be Connected! 
- No Cycles
- Max amount of edges should be n - 1 

BFS SOLUTION

NOTE: node 0 is given to us by default!!
"""

from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # max amount of edges
        if len(edges) > n - 1:
            return False 



        # We want to build our adjacency list using a list of size = nodes
        adjacency_list = [[] for i in range(n)]
        # bidirectional 
        for u, v in edges: 
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        # queue will hold parent and current node 
        queue = deque()
        queue.append([0, -1])
        visit = set() 
        visit.add(0)

        while queue: 


            current_node, parent_node= queue.popleft()

            for the_neighbours_of_current_node in adjacency_list[current_node]: 

                # if we have two nodes that equal each other in this list, it is expected and they are just bidirectional ndoes, thats why we are even storing the paretn_ndoe in the first place! 
                if the_neighbours_of_current_node == parent_node: 
                    # Skip the entire loop 
                    continue 

                # now if we are in visisted, this implicates a cycle!
                if the_neighbours_of_current_node in visit: 
                    return False 
                
                visit.add(the_neighbours_of_current_node)
                queue.append([the_neighbours_of_current_node, current_node])

        # if we haven't reached false by that point, then the only edge case left is that len(visit) must ensure that we visited all nodes, else we return False! 

        return len(visit) == n 

        





        
        