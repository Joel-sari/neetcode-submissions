class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        result = []
        adj_graph = {}
        parent_count = {}

        for i in range(numCourses):
            if i not in adj_graph:
                adj_graph[i] = []
                parent_count[i] = 0
            
        for child, parent in prerequisites:
            adj_graph[parent].append(child)
            parent_count[child] += 1
        
        for node in parent_count:
            if parent_count[node] == 0:
                q.append(node)
        
        while q:
            curr = q.popleft()
            result.append(curr)
            for child in adj_graph[curr]:
                parent_count[child] -=1
                if parent_count[child] == 0:
                    q.append(child)

        if len(result) == numCourses:
            return result
        else:
            return []
            