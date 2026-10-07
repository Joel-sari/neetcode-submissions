class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        temp = image[sr][sc]
        image[sr][sc] = color

        rows = len(image)
        cols = len(image[0])

        

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] in visited:
                return
            
            if image[r][c] == temp:
                image[r][c] = color
            
            visited.add(image[r][c])

            if image[r][c] == color:
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            return

        
        dfs(sr, sc)

        return image