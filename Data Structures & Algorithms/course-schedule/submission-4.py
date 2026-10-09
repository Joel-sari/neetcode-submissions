class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        result = 0
        q = deque()
        adj_graph = {}
        parent_count = {} #for each child

        for child, parent in prerequisites:
            if parent not in adj_graph:
                adj_graph[parent] = []
                parent_count[parent] = 0
            
            if child not in adj_graph:
                adj_graph[child] = []
                parent_count[child] = 0
        
        for child, parent in prerequisites:
            adj_graph[parent].append(child)
            parent_count[child] += 1
        
        for node in parent_count:
            if parent_count[node] == 0:
                q.append(node)
        
        while q:
            curr = q.popleft()
            result += 1
            for child in adj_graph[curr]:
                parent_count[child] -= 1
                if parent_count[child] == 0:
                    q.append(child)
        
        return result == len(adj_graph)

    
