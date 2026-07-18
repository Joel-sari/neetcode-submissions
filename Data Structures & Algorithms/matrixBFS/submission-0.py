class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Lots of data structure set up to allow for our BFS to work
        # hashset to ensure we dont visit the same coordinate twice
        visited = set()

        #QUEUE is necessary, but why? we need to must understand that we are going at a level order traversal
        # we look at adjacent nodes, and go through them in order
        queue = deque()

        # We initially start our queue at the first top left coordinate! (satrting point)
        queue.append((0,0))
        visited.add((0,0))

        # this will keep track of the length of our path!!
        length = 0 

        # while we have adjacent values to check!
        while queue:
            for index in range(len(queue)):
                current_row, current_col = queue.popleft() # what does this do? it gives us the coordinates of the queue !
                
                # check if we have finally reached the end point!!
                if current_row == rows - 1 and current_col == cols - 1:
                    # if so we can finish and just return the length 
                    return length

                             # right                          #down                           # left                            #up
                direction = [[current_row + 1, current_col], [current_row, current_col + 1], [current_row - 1, current_col ], [current_row, current_col - 1]]
                for direction_row, direction_col in direction:
                    # check if we out of bounds on the lower end
                    if (min(direction_row, direction_col) < 0 or
                    # check if we out of bounds on the upper end
                        direction_row == rows or direction_col == cols or 
                        (direction_row, direction_col) in visited or 
                        # if we reach a rock yeah we need to skip tf out of it
                        grid[direction_row][direction_col] == 1):
                        continue 
                    
                    # continue would skip over this! 
                    queue.append((direction_row, direction_col))
                    visited.add((direction_row, direction_col))
                    
            length += 1
        return -1

                






        