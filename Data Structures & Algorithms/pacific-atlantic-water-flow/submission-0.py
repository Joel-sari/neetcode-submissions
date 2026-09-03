"""
Problem defintion: 

- We need to find the route from atlantic ocean to pacific ocean 

- a path is valid from the pacific/atalantic if the grid height[r][c] is in an increasing order (the middle value must be the largest, thinkl about it like the middle going to the border, if the heigh on it's way is larger, than we know it's a wall that is blocking us off)


Our approach: 

we will run DFS twice, on both the atlantic side (bottom) and pacific side(top) ! we know our movements are up, down, left, right. So we will run dfs on those 

- if there is a visited that already exists after running it on pacific side and we come accross it agin for the atlantic side, then we know we have found a path


"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row_border, col_border = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        directions = [[1,0], [0,1], [-1,0], [0,-1]]


        def dfs(row, col, visited_grid_spots, previous_height): 
            if ((row, col) in visited_grid_spots or
                row == row_border or 
                col == col_border or 
                min (row, col) < 0 or
                # lastly we need to account / only be allowed to go to heights bigger than the previous one 
                heights[row][col] < previous_height):
                return 
            visited_grid_spots.add((row, col))


            for d_row, d_col in directions: 
                dfs(row + d_row, col + d_col,visited_grid_spots, heights[row][col])


                 



        # Here we are gonna grab all the (r,c) values in our pacific set 
        for col in range(col_border):
            # calling dfs on our pacific ocean top border!
            dfs(0, col, pacific, heights[0][col])

            # calling dfs on our atlantic coean bottom border 
            dfs(row_border - 1, col, atlantic, heights[row_border - 1][col] ) 

        # NOW we also need to remember that we need to keep in mind we need to enter the first column and the last, the last = atlantic and the first = pacific

        for row in range(row_border): 
            #pacific ocean dfs 
            dfs(row, 0, pacific, heights[row][0] )
            #atlantic ocean dfs 
            dfs(row, col_border - 1, atlantic, heights[row][col_border - 1] )

        
        # lastly we need to create our result our array by going through each point (r, c) in the graph, and see if they are in both visited sets, if so, that indictaes a valid square that has a clear path between pacific and atlantic 
        valid_points_that_make_the_path = []
        for r in range(row_border): 
            for c in range (col_border):
                if ((r,c) in pacific and (r,c) in atlantic):
                    valid_points_that_make_the_path.append([r,c])

        return valid_points_that_make_the_path


        
        