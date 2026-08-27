"""
0 - land
1 - rocks, cannot be traversed 

return the number of unique paths from top left corner to bottom right corner.

NOTE: we dont finish at bottom right corner! 
we finish when all paths have been exhausted


"""
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        max_row, max_col = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        
        

        def dfs(r, c, visited_spots): 
            if( r == max_row or 
                c == max_col or 
                min(r, c) < 0 or 
                grid[r][c] == 1 or 
                (r, c) in visited_spots
            ): 
                return 0 

            if r == max_row - 1 and c == max_col - 1: 
                return 1
            visited_spots.add((r, c))

            unique_paths = 0 
            for dir_x, dir_y in directions: 
                unique_paths += dfs(r + dir_x, c + dir_y, visited_spots)
            # Dont forget to unmount/backtrack 
            visited_spots.remove((r, c))
            return unique_paths
            
        # We are starting the algorithm starting from the beginning of the matrix
        return dfs(0, 0, set())
        