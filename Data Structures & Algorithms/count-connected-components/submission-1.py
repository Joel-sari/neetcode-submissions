class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjacency_list = [[] for node in range(n)]

        visited = set() 

        # building out the adjacency list of lists 
        for node1, node2 in edges: 
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        
        def bfs(node): 
            queue = deque([node])
            visited.add(node)

            while queue: 
                cur_node = queue.popleft() 
                for neighbour in adjacency_list[cur_node]: 
                    if neighbour not in visited: 
                        visited.add(neighbour)
                        queue.append(neighbour)


        
        result = 0 

        for node in range(n): 
            if node not in visited: 
                visited.add(node)
                bfs(node)
                result += 1


        return result
        