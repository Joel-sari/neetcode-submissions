"""
The idea behind this is using the prefix of row[i]col[j] and row[i+1]col[j]

we are essentially creating a matrix of our own using prefxi values to retrieve the asnwer in constant time 

"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix_rows, prefix_cols = len(matrix), len(matrix[0])

        # Now we are creating prefix matrix intializing everything to be 0 and again it is one row and colum bigger
        self.prefixMatrix = [[0] * (prefix_cols + 1) for row in range(prefix_rows+1)]

        
        
        # Note we have an extra row and column so we hav eto ensure we offset by one on both sides when putting it into our newly created prefixMatrix, the range can stay the same
        for row in range(prefix_rows):
            prefix = 0
            for column in range (prefix_cols):
                prefix += matrix[row][column]
                
                # NOTE: lets thing back to what the idea of a prefix is, it is again basically your are taking subarray sums and subtract them to get a spliced sub array you want 
                # here Note we have a 2D Problem, hence we also need to take our above value and add it to our prefix, since the same thing will happen when tryna to get the prefix difference 
                #we will be subtracting the values to get the total sum of that sub area of the matrix. It's just a prefix problem but in 2D  

                above = self.prefixMatrix[row][column + 1]
                self.prefixMatrix[row+1][column + 1] = prefix + above 

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Okay so before, first thing s first we want to easily navigate through our matrix above in which we created! lets update our retrieving indices to match our matrix
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1 ,col2 +1

        # Now we want to get the area of the matrix! BUT NOTE WE ARE GETTING THE AREA OF THE "OUTER" sides of the OG matrix, but correclty in bounds in our prefixMatrix 
        # Why? because we need to subtract these areas to get the correct value which we'll see later

        """
        Note it would look something like this , the regular matrix would just be 3*3 of ones

   top Left ->  0 0 0 0 <- Top Right
                0 1 2 3
                0 4 5 6
bottom Left ->  0 7 8 9 <- bottom Right

        
        """

        #  
        bottomRight = self.prefixMatrix[row2][col2]

        #we get the above value, meaning the top right corner 
        topRight = self.prefixMatrix[row1-1][col2]


        bottomLeft = self.prefixMatrix[row2][col1-1]
        topLeft = self.prefixMatrix[row1-1][col1-1]
        return bottomRight - topRight - bottomLeft + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)