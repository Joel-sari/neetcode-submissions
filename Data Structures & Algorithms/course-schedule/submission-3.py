class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #prereq [dependent, dependency]
        result = 0
        q = deque()
        adj_graph = {}
        dependency_count = {} 

        for child, parent in prerequisites:
            if child not in adj_graph:
                adj_graph[child] = []
                dependency_count[child] = 0
            if parent not in adj_graph:
                adj_graph[parent] = []
                dependency_count[parent] = 0

        for child, parent in prerequisites:
            adj_graph[parent].append(child)
            dependency_count[child] += 1

        for course in adj_graph:
            if dependency_count[course] == 0:
                q.append(course)
        
        while q:
            curr = q.popleft()
            result += 1
            for child in adj_graph[curr]:
                dependency_count[child] -= 1
                if dependency_count[child] == 0:
                    q.append(child)
        
        if result == len(adj_graph):
            return True
        return False
            

        

        



