class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        starting_point = image[sr][sc]

        self.dfs_helper(image, sr, sc, color, starting_point)

        return image 
        
        

    def dfs_helper(self, image, sr, sc, color, starting_point):

        row_boundary = len(image)
        col_boundary = len(image[0])
        lower_row_boundary, lower_col_boundary = 0, 0 

        if (sr < lower_row_boundary 
            or sr >= row_boundary 
            or sc < lower_col_boundary 
            or sc >= col_boundary
            # this condition is cause we kept the starting_point (which in one of the examples was 1, there could be a chance that we are not guaranteed to have a pixel == 1, thus we keep track of the value of the starting point)
            or starting_point != image[sr][sc] 
            # meaning we already color filled this pixel
            or image[sr][sc] == color): 
            return
            

        #else we color fill
        image[sr][sc] = color

        # We need to move in all 4 directions
        self.dfs_helper(image, sr + 1, sc, color, starting_point)
        self.dfs_helper(image, sr - 1, sc, color, starting_point)
        self.dfs_helper(image, sr, sc + 1, color, starting_point)
        self.dfs_helper(image, sr, sc - 1, color, starting_point)
        

        
        