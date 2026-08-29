"""
Constraints: 

- No self edges (meaning no self closing nodes)
- More than one edge in a vertex connection isn't allowed 
- graph can have cycles 
- graph doesn't have to be necessarily all connected 

many ways to implement graphs, easiest way is using adjacecny lists
"""
from collections import defaultdict, deque

class Graph:
    
    def __init__(self):
        self.adjacency_list = defaultdict(set)


    def addEdge(self, src: int, dst: int) -> None:
        # no self closing edges
        if src == dst: 
            return
        self.adjacency_list[src].add(dst)
        

    def removeEdge(self, src: int, dst: int) -> bool:
        # we cant remove anything that isn't in our adjacency list
        # or the source given doesn't have a neighbour connected to it, we do this check through the adjacency list
        # NOTE THAT WE MADE IT A SET (the adjacency list), this makes checking if it's in the set O(1) time 
        if src not in self.adjacency_list or dst not in self.adjacency_list[src]: 
            return False
        self.adjacency_list[src].remove(dst)
        return True
    def hasPath(self, src: int, dst: int) -> bool:
        # multiple ways to determine if we have the path to the destination given
        # we will use BFS 
        if src == dst: return True
        visited_nodes = set() 
        visited_nodes.add(src)

        queue = deque()
        queue.append(src)

        def bfs(src, dst):

            while queue: 
                for i in range(len(queue)): 
                    current_node = queue.popleft()
                    for neighbour in self.adjacency_list[current_node]: 
                        if neighbour == dst: 
                            return True 
                        if neighbour not in visited_nodes:
                            visited_nodes.add(neighbour)
                            queue.append(neighbour)
            return False

        return bfs(src, dst)
