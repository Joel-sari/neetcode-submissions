from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:


        # Defining out boundaries
        row_max, col_max = len(grid ), len(grid[0])

        # we need a set to handle land that we have already visited 
        land_visited = set()

        # we need a queue to take care of our level ordered search 
        queue = deque()

        # We need to intiiate our set and queue to have our starting point already, else the while loop wouldn't even start, note if it isn't a 0 then we have no need to search the grid cause we would fail 
        if grid[0][0] == 0:
            queue.append((0,0))
            land_visited.add((0,0))

        directions = [[0,1], [1,0], [0,-1], [-1,0]]


        def bfs(grid): 
            length = 0
            while queue:
                
                for i in range(len(queue)): 
                    row, col = queue.popleft() 

                    if row == row_max - 1 and col == col_max - 1: 
                        return length 

                    for dir_x, dir_y in directions: 
                        new_row = row + dir_x
                        new_col = col + dir_y 
                        if (new_row == row_max or 
                            new_col == col_max or 
                            min(new_row, new_col) < 0 or
                            grid[new_row][new_col] == 1 or 
                            (new_row, new_col) in land_visited):
                            # we continue through our other possible directions 
                            continue
                        queue.append((new_row, new_col))
                        land_visited.add((new_row,new_col))
                length += 1 
                    
            return -1

        return bfs(grid)


        