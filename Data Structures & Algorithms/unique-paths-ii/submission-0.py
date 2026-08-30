# Lets use a bottom up approach, using DP

# m = rows 
# n = cols
"""

when we first start: 

current-row = 0,0,0,1

previous row =0,0,0,0


grid built out: 
obstacleGrid = 
[[0,0,0],
 [0,0,0],
[0,1,0]]

Essentially the same sort of idea but with one more condition now, that we can't come across a 1

I wonder if we can use the bottom up approach still lets try it,

maybe if we skip it if we come by a 1? 


"""
class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # Grabbing our dimensions first 
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        # for tracking purposes
        previous_bottom_row = [0] * cols 

        # we will initialize our previous_bottom_row to have a value of 1 if there is a 0 on the destination of the robot on the grid 
        if obstacleGrid[rows - 1][cols - 1] == 0:
            previous_bottom_row[cols - 1] = 1 
        else: 
        # this whole matrix is invalid otherwise 
            return 0

        
        for row in range(rows - 1, -1, -1): 
            # this will be the row we update with most recent path data 
            current_row = [0] * cols 
            if obstacleGrid[row][cols - 1] == 1: 
                current_row[cols - 1] = 0
            # this doesn't mean we have a valid path, we need to take the previous rows left value cause it could be that there was an obstacle way further down  taht completely disregards any path strictly on the left side of the grid
            else: 
                current_row[cols - 1] = previous_bottom_row[cols - 1]

            for col in range(cols - 2, -1 , -1): 
                if obstacleGrid[row][col] == 1: 
                    continue 
                current_row[col] = current_row[col + 1] + previous_bottom_row[col]
            previous_bottom_row = current_row
        return current_row[0]


                

                






       