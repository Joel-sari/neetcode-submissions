"""

This is an example of BFS (Searching as many places as you can)

Remmeber BFS uses a Queue to keep track of our visited nodes.



"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        # iniatilizing how many rows and columns there are!
        rows, cols = len(grid), len(grid[0]) 

        # keeps track of visited couples, notice the use of a set
        visited = set()   

        # keeping track of the number of islands
        islands = 0 

        def bfs(r, c):
            # this is the data structure we use to keep track of our queue

            # collections.deque() starts a queue for us 
            queue = collections.deque()

            visited.add((r, c))
            queue.append((r, c ))

            while queue: 

                # this pops the queues couple values into row and col
                row, col = queue.popleft()
                directions =[[1,0],[-1,0], [0,1],[0, -1]]

                for direction_r, direction_c in directions:

                    # These values/calculations will hold all possible neighbours
                    # and add to 
                    r, c = row + direction_r, col + direction_c

                    if (r in range(rows) and  c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))

        # we want to vist through every position in the grid
        for r in range(rows):
            for c in range(cols):
                # if we visit a 1 we have to do BFS and then also need to make sure its not 
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands

    
        