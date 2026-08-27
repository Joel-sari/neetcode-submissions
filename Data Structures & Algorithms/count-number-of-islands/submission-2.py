"""
The algorithm to this is basically:
1. To use a normal double for loop to scan the martix for island, 
    1.1 - ensure we have a set(of visited points that make up the island) to not run dfs on it again
    1.2 - it will run until the "1" value we find then,
2. run a dfs/ or bfs algorithm that returns once we have fully visited the island, 
    2.1 - NOTE, we do NOT return ANYTHING
    2.2 - Simply we are using DFS as an EXPLORER that runs UNTIL THE WHOLE ISLAND IS EXPLORED , then returns. 
    2.3 - What is being changed is the set of values, which is evaluated with the out double for loop

3. return the count of island 



"""

class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int: 
                      #down   #right  #up     #left
        directions = [[0,1], [1,0], [0, -1], [-1, 0]]

        #Our boundaries 
        max_rows, max_cols, min_rows, min_cols = len(grid), len(grid[0]), 0, 0

        if not grid: 
            return 0 

        # Store sets of tuples (r,c)
        visited_spots = set()
        number_of_islands = 0 

        # think of dfs in this problem as just an explorer! Not as someone who returns the count of islands because that is something our outer functions does!
        def dfs(row, col): 

            # our exiting case
            if (min(row, col) < 0 or 
                row == max_rows or 
                col == max_cols or 
                grid[row][col] == "0" or 
                (row, col) in visited_spots):
                return


            visited_spots.add((row, col))

            # to run dfs in a more organized manner, lets use our directions array,and loop through the different paths 
            for direction_horizontal, direction_vertical in directions: 
                dfs(row + direction_horizontal, col + direction_vertical)

            
            


        # outer for loop
        for r in range(max_rows): 
            for c in range(max_cols): 
                # if case so that we don't revist any land that has already been accounted for an island
                # and that it is actual land 
                if grid[r][c] == "1" and (r, c) not in visited_spots: 

                    number_of_islands += 1
                    dfs(r, c)

        return number_of_islands






