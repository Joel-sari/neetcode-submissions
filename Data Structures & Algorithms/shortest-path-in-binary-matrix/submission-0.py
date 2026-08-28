
"""
Goal: 
- return a clear path, this is binary matrix (means 0s and 1s only)
- we need to start top-left cell
- Best algorithm for shortest path = BFS
- 8 DIRECTIONAL ( so we can move diagonally)


"""
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # Dimensions/ Boundaries of our grid
        n = len(grid)


        # make use of a hash set, which will carry tuples for coordinates
        visited_squares = set() 

        queue = deque() 

        eight_directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,1],[-1,-1],[1,-1]]


        if grid[0][0] == 0: 
            queue.append((0,0))
            visited_squares.add((0,0))

        shortest_path = 1

        while queue: 
            for current_square in range(len(queue)):
                curr_r, curr_c = queue.popleft()

                if curr_r == n - 1 and curr_c == n - 1: 
                    return shortest_path

                for r, c in eight_directions: 
                    # this is the direction calculation
                    new_r = curr_r + r 
                    new_c = curr_c + c

                    # here are our checks for whether we count this shortest_path 
                    if (min(new_r, new_c) < 0 or 
                        max(new_r, new_c) == n or 
                        grid[new_r][new_c] == 1 or 
                        (new_r, new_c) in visited_squares): 
                        continue 
                    visited_squares.add((new_r, new_c))
                    queue.append((new_r, new_c))
                
            shortest_path += 1 


        return - 1





        