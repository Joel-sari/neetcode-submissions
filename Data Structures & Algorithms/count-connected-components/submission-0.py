from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0 or edges is None: 
            return 0 
        
        adjacency_list = [[] for node in range(n)]

        visited = set()

        # building our adjacency list 
        for node1, node2 in edges: 
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        def dfs(node): 
            for neighbour in adjacency_list[node]: 
                if neighbour not in visited: 
                    visited.add(neighbour)
                    dfs(neighbour)
        
        result = 0 

        for node in range(n): 
            if node not in visited: 
                visited.add(node)
                dfs(node)
                result += 1 

        return result

        