"""
BOTTOM UP SOlUTION: 

Algorithm/Intuition: 

Summary:

1. - Basically we are going to create a grid copyish like to cache the value we are trying to compute for longest common substring betweeen both texts

2. - we then calculate (using the fact that we only down right), up and left the count, we say that when both texts[i] equal eachother, we are complete 

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        


        # So here we are creating a 2 D grid with an extra row + column that again will serve as the bounds value (of zero) to be used in algorithm for bottom up
        empty_2D_grid = [[0] * (len(text2) + 1) for character in range(len(text1) + 1 )]
        # text2 is the colums 
        # text1 is the row
        for row in range(len(text1) - 1, -1, -1):
            for col in range(len(text2) -1, -1, -1):
                if text1[row] == text2[col]: 
                    empty_2D_grid[row][col] = 1 + empty_2D_grid[row+1][col+1]

                else: 
                # what are we doing then? finding the max values of bottom and right side and then just making part of the grid 
                    empty_2D_grid[row][col] = max(empty_2D_grid[row+1][col], empty_2D_grid[row][col + 1] )

            
        return empty_2D_grid[0][0]



         
        