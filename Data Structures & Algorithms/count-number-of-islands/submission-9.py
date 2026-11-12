from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Input validation 
        if not grid: 
            return 0 

        # we need to get our dimensions 
        rows, cols = len(grid), len(grid[0])
                    # right  down    left    up   
        directions = [[1,0], [0,1], [-1, 0,], [0, -1]]
        

        # We need to mark visited pieces of islands 
        visited_land = set()

        island_count = 0 

        def bfs(row, col): 

            queue = deque()

            visited_land.add((row, col))

            queue.append((row, col))

            while queue:
                # Notice we are poopping from the left fifo
                current_row, current_col = queue.popleft()

                # Now we need to ensure all our edge cases are being handled correctly including boundaries + 
                

                for dir_row, dir_col in directions: 

                    new_row_dir, new_col_dir = dir_row + current_row, dir_col + current_col
                    
                    if (new_row_dir in range(rows) and 
                        new_col_dir in range(cols) and 
                        grid[new_row_dir][new_col_dir] == '1' and 
                        (new_row_dir, new_col_dir) not in visited_land):
                        queue.append((new_row_dir, new_col_dir))
                        visited_land.add((new_row_dir, new_col_dir))


        for row in range(rows): 
            for col in range(cols): 
                if grid[row][col] == '1' and (row, col) not in visited_land: 
                    bfs(row, col)
                    island_count += 1

        return island_count
                    