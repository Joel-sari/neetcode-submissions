class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        # getting the dimensions of the grid!
        rows, cols = len(grid), len(grid[0])

        # DFS
        def dfs_helper(grid, row, col, visited):

            # there are multiple base cases, that cause our path to end!:
            # 1. Out of bounds either left or up, or bottom and right 
            # 2. A rock we come across (ends path cause we crashed)
            # 3. if we have visited that path then that recursive section should return 0 too
            if (row < 0 or 
                col < 0 or 
                row == rows or 
                col == cols or 
                grid[row][col] == 1 or 
                (row, col) in visited):
                    return 0 
            

            # this is if we reached the end corner succesfully!
            if row == rows - 1 and col == cols - 1:
                return 1
            
            # We will add to our hashset the tuple of row and column to let it know we have come across 
            # this coordinate already
            visited.add((row, col))


            # we initialize a count variable that will be added if we have a succesful path else 
            count = 0 

            # There are four different directions the path can go!!
            # right direction
            count += dfs_helper(grid, row + 1, col, visited)
            # down direction
            count += dfs_helper(grid, row, col + 1, visited)
            # left direction 
            count += dfs_helper(grid, row - 1, col, visited)
            # up direction
            count += dfs_helper(grid, row , col - 1, visited)

            # Allows for backtracking, without this we wouldn't be able to look at other paths 
            visited.remove((row,col))

            return count
            

        
            
            


                


        

        return dfs_helper(grid, 0, 0, set())