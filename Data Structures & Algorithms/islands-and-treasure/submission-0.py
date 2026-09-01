from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        INF = 2147483647

        # defining our dimensions first 
        row_max, col_max = len(grid), len(grid[0])
        queue = deque()
        visited_spaces = set() 

        # here we are adding all infiniti movements as well into the queue!
        # NOTE, we do it 1 by 1  
        def addCell(row, col): 
            # return out if we hit out of bounds OR VISITED, VISITED IS REALLY IMPORTANT ALTHOUGH SOUNDS VERY GEENRIC, but because we are running through the scan simultaneously, we need to make sure there is no collision
            if (min(row, col) <  0 or 
                row == row_max or  
                col == col_max or 
                (row,col) in visited_spaces or
                grid[row][col] == -1): 
                return
            # Else we should jsut add it into our visited as we traverse too
            visited_spaces.add((row, col))
            queue.append((row,col))

        for row in range(row_max): 
            for col in range(col_max): 
                if grid[row][col] == 0:
                    # these are the treasure chest points we are going to run bfs on 
                    queue.append((row, col))
                    visited_spaces.add((row, col))

        distance = 0 
        # we start by going through our FIFO'd treasures and then positioning from there
        # they way it works "simultneaously" is by going 
        while queue: 
            for i in range(len(queue)): 
                # queue will always have the next best spot to go to 
                row, col = queue.popleft() 
                grid[row][col] = distance 
                addCell(row + 1, col)
                addCell(row, col + 1)
                addCell(row -1 , col)
                addCell(row, col - 1)

            distance += 1



        


        

        