class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
         # renaming things 
        rows, cols = m, n 

        # Why are we multiplying by cols only? Cause cols defines how many spots (cols) per row
        previous_bottom_row = [0] * cols 
        # now we need to iterate backwards! from bottom left to top right
        for row in range(rows - 1, -1, -1):
            current_row = [0] * cols 

            # Our base case, we always want our right most to be 1 since that will never change due to the established down and right only movements 
            current_row[cols - 1] = 1

            # Now we can loop through each col in the currentRow and update it's values accordingly! 
            # NOTE: we start at - 2 cols cause we already set up our last value to the right  to be 1 by default always
            for col in range(cols - 2, -1, -1): 
                # we update by adding values from bottom and right kind alike this shape: 
                """
                 + -> current_row [index + 1] right side
                 |
                prev_row[c] down 
                """
                current_row[col] = current_row[ col + 1 ] + previous_bottom_row[col]

            # once this loop finishes and we have updated all cols in the row, we can update previous row to be the current and create a new currentRow at the top thats empty! 
            previous_bottom_row = current_row 

        # this will be the top right most value 
        return current_row[0]


        
        