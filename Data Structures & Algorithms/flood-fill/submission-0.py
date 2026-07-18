class Solution:
    """
    BASICALLY the problem is saying that sr and sc are given, these is your i and j of 
    where to go in the matriz, the color is what you change the pixels to. You must change
    every pixel THAT MATCHES THE STARTING PIXEL's value into teh GIVEN COLOR! EVRYTHING ELSE MUST NOT CHANGE

    [1,1,1]     [2,2,2]
    [1,1,0] ->> [2,2,0]
    [1,0,1]     [2,0,1]
    
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # So lets distince the starting pixel location
        starting_pixel = image[sr][sc]
        
        # First we need to change the color of this starting point, but how do we iterate 
        # and check if all other pixels are match the starting_points value?



        self.dfs(image, sr, sc, color, starting_pixel)

        # afte the recursive DFS called we can return the modified image

        return image
        # DEPTH FIRST SEARCH 

    def dfs(self, image, sr, sc, color, starting_pixel):

        """
        These are the conditions: 
        1.  we must be in bounds. Thus,  sc < 0 or sr < 0 or sc < len(image[0]) sr < len(image)
        2. the pixel cannot match the color, if it does we are done,
        3. the pixel must match the starting_pixel, only those can be changd

        So if none of this conditions we returnj out the dfs
                
        """
        if sc < 0 or sr < 0 or sc >= len(image[0]) or sr >= len(image) or starting_pixel != image[sr][sc] or image[sr][sc] == color:
            return

        # this changes the color of the point in the matrix we are on
        image[sr][sc] = color

        # Move up in the matrix 
        self.dfs(image, sr+1, sc, color, starting_pixel)
        #Move down in th matrix
        self.dfs(image, sr-1, sc, color, starting_pixel)
        # Move right in the matrix 
        self.dfs(image, sr, sc+1, color, starting_pixel)
        #Move left in th matrix
        self.dfs(image, sr, sc-1, color, starting_pixel)
            