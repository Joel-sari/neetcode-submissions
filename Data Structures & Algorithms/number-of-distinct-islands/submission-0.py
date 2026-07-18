"""
The problem we have is a bfs problem that involves also keeping track 
of the shape of certain islands. Thus our inner bfs function should return a tuple 
into a visited_islands, we then of course keep track of this count 
"""

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        # This will hold the bounds of the grid, so we can check to make 
        # when we search we stay in bounds 
        row_bounds, column_bounds = len(grid), len(grid[0])

        # Keep a count total Unique visited_islands
        number_of_unique_islands = 0 


        # To ensure we don't visit the same island again we keep track of the visited islands using 
        #   hash set 

        visited_land = set() 
        number_of_shapes = set()

        def bfs(starting_row, starting_column):
            queue = collections.deque() 

            # This will hold the offset/distance values from the original island starting point 
            # This will help us figure out the shape of the island by arranging the list with tuples of offset
            # this list will eventually be stored in a tuple and if the shape matches another island 
            #when tried to be added to our outer hashset, it will fail since it exists already
            shape_of_current_island = []

            # we need to add this new visited land into our visited to ensure we dont check back here 
            visited_land.add((starting_row, starting_column))

            queue.append((starting_row, starting_column))
            
            
            # While our queue still holds values, meaning we are in constant finding of coming across
            # adjacent neighbours.
            while queue: 

                # remmeber we always have to pop the one we are dealing with in the queue 
                current_row, current_column = queue.popleft()


                # We are calculating the offset FROM THE STARTING POINT OF THE ISLAND 
                offset_from_starting_row = current_row - starting_row
                offset_from_starting_column = current_column - starting_column

                shape_of_current_island.append((offset_from_starting_row, offset_from_starting_column))

               


                # Then we need to have the directions or moves and go through each 
                # to see if how many adjacent pieces of lands there are 
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for move_vertical, move_horizontal in directions:


                    # We also need to calcula

                    new_row, new_column = current_row + move_vertical, current_column + move_horizontal

                    if (new_row in range(row_bounds) and
                        new_column in range(column_bounds) and 
                        (new_row, new_column) not in visited_land and 
                        grid[new_row][new_column] == 1):
                        # Now we have to also appened to our queue to keep track of possible lands that we mauy need to visit after

                        queue.append((new_row, new_column))
                        visited_land.add((new_row, new_column))
            
            # We sort this so that we reach a level of consistency for identical shape_of_current_island
            # This is neccessary because the way we store stuff in our queue isn't consistent an it could mess up our shape identifier
            shape_of_current_island.sort()
                        
            return tuple(shape_of_current_island)


        
        for row in range(row_bounds):
            for column in range(column_bounds):
                if grid[row][column] == 1 and (row, column) not in visited_land: 
                    number_of_shapes.add(bfs(row, column)) 
    
        return len(number_of_shapes)


                    


        