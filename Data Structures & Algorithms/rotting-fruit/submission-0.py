from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # dimensions/boundaries to our grid 
        row_max, col_max = len(grid), len(grid[0])

        

        

        # directions array (hor and vert)
        directions = [[0,1], [1,0], [0, -1], [-1,0]]

        fresh_fruit_counter = 0

        queue = deque()

        total_time = 0 

        
        # first we need to scan the matrix and get all the rotten fruits, add them to our queue so we can simultaneously go through eache level and add minutes, change them to rotten
        for r in range(row_max): 
            for c in range((col_max)): 
                if grid[r][c] == 2: 
                    queue.append((r,c))
                elif grid[r][c] == 1: 
                    fresh_fruit_counter += 1
                    


        while queue and fresh_fruit_counter > 0: 
            for i in range(len(queue)): 
                curr_row, curr_col = queue.popleft()
                for dir_r, dir_c in directions: 
                    new_row, new_col = curr_row + dir_r, curr_col + dir_c
                    if (min(new_row, new_col) < 0 or 
                        new_row == row_max or 
                        new_col == col_max or 
                        grid[new_row][new_col] == 0 or 
                        grid[new_row][new_col] == 2):
                        continue
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 2
                    fresh_fruit_counter -=1
                
            total_time += 1

        # There is an edge case in which we have a fruit that isn't adjacent to a rotten  fruit. Then we have failed and can return - 1
        if fresh_fruit_counter > 0: 
            return -1 

        return total_time







        