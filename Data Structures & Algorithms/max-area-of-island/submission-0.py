"""
- This is very similar to number of Islands, but instead we need to not only explore, but return the area of each island, 

- In the outer loop we will just use the max function to compare both the returning dfs 

"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        

        #             down   right     up     left
        directions = [[0,1], [1,0], [0, -1], [-1,0]]
        row_max, col_max, row_min, col_min = len(grid), len(grid[0]), 0, 0

        visited_spots = set() 




        def dfs(row, col): 
            if (row == row_max or 
                col == col_max or 
                min(row, col) < 0 or 
                grid[row][col] == 0 or 
                (row, col) in visited_spots):  
                    return 0
            # area = 1 as it is defined as soon as we move our "pointer" to the next square spot 
            area = 1 
            visited_spots.add((row, col))

            for dih_x, dih_y in directions: 
                # its only here when we start backtracking and addding our area = 1 to the previous area's calculation
                area += dfs(row + dih_x, col + dih_y)   
            # now we return area 
            return area 


        
        max_area = 0

        for row in range(row_max):
            for col in range(col_max):
                if grid[row][col] == 1 and grid[row][col] not in visited_spots: 
                    potential_new_max_area = dfs(row, col)
                    max_area = max(max_area, potential_new_max_area )

        return max_area






    

        