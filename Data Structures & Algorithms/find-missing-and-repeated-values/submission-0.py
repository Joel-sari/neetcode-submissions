# We are given a grid of values 
"""
And what the problem is mainly looking for is having all the values from range 1...n^2

thus if we have a 2x2 grid we would expect a 1,4 range

we will be missing one value and have a repeating value


we need to return [twice, missing]


"""
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dimension_of_grid = len(grid)

        # by doing this we are allowed to add to hashmap even when a key may not exist!
        count_of_each_num = defaultdict(int)

        # We create the COUNTER aka hashmap that maps the key to the count, 
        # NOTE: we are manually doing it here and with the valyes in the grid 
        for row in range(dimension_of_grid):
            for column in range(dimension_of_grid):
                count_of_each_num[grid[row][column]] += 1

        twice, missing = 0,0

        for num in range(1, dimension_of_grid*dimension_of_grid + 1):
            # Even tho this count "may not exist" using default dict allowed it to exist!!
            # This is important to understand!
            if count_of_each_num[num] == 0:
                missing = num

            if count_of_each_num[num] == 2:
                twice = num
        
        return [twice, missing]

        

        