"""
DFS Version

same process just different process + recursion! 

"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjacency_list = [[] for i in range(n)]

        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u) 

        


        visit = set()
        
        def dfs(current_node, parent_node): 
            # Base case, cycle detection
            if current_node in visit: 
                return False 
            
            visit.add(current_node)
            
            # Now we want to go through our adjacency list 
            for neighbors_of_current_node in adjacency_list[current_node]: 
                

                # skip over the ones that equal each other (the bidirectional edges)
                if neighbors_of_current_node == parent_node: 
                    continue 
                if not dfs(neighbors_of_current_node , current_node): 
                    return False
            

            return True
        return dfs(0, -1) and len(visit) == n