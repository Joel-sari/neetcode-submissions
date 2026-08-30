class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n 
        # the way we want to cache our values is creating the grid our selves with values 
        cache = [[-1] * cols for row in range(rows)]

        def dfs(row, col): 
            # we need our base case which is if we out of bounds 
            if row == m or col == n: 
                return 0 # not a valid unique path 
            
            # Now we can check if our value is already part of our matrix cache/grid that is already keeping track of our values. as long as it has a value, it means it's already been accounted for  
            if cache[row][col] != -1: 
                return cache[row][col]
            
            # now we need a valid path, and return 1 
            if row == m - 1 and col == n -1:
                return 1 
            
            # recursive movement, we going to return the addition of all movements
            cache_result = (dfs(row + 1, col) + dfs(row, col + 1))

            cache[row][col] = cache_result

            return cache_result

        return dfs(0, 0)
        
        