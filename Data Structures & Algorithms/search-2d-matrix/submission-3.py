"""
Basically this algorithm is running through binary search twice 
on the row and on the column

basically we choose a row, check if we are in the right row by checking if the value even falls in between the row or not. 
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # first we need to get the dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # we run binary search vertically in a way 
        top_row_pointer, bottom_row_pointer = 0, ROWS - 1

        while top_row_pointer <= bottom_row_pointer: 
            # Binary search on a row
            selected_mid_row = (top_row_pointer + bottom_row_pointer) // 2

            # NOTE, matrix[selected_mid_row][-1] is the greatest integer in the row!!
            if target > matrix[selected_mid_row][-1]: 
                top_row_pointer = selected_mid_row + 1
                
            # NOTE, matrix selected_mid_row [0] is the smallest integer in the row
            elif target < matrix[selected_mid_row][0]:
                bottom_row_pointer = selected_mid_row - 1
            # in this case we are in the right row or we have exhausted all rows and our target is out of bounds
            else: 
                break 
        
        # Now that we are out of the loop, lets check that our rows equal eachother (meaning we found a row, else if they dont, we can retrun false)
        if not (top_row_pointer <= bottom_row_pointer):
            return False
        
        succesful_row = (top_row_pointer + bottom_row_pointer) // 2

        left_pointer, right_pointer = 0, len(matrix[succesful_row]) -1 

        # Now we run the regular binary search
        while left_pointer <= right_pointer: 

            midpoint = (left_pointer + right_pointer) // 2

            if target < matrix[succesful_row][midpoint]:
                right_pointer = midpoint - 1

            elif target > matrix[succesful_row][midpoint]:
                left_pointer = midpoint + 1
            else:
                return True 
        return False


           


            
            
        
        


            
            





        