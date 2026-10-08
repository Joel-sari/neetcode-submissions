class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
 
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        length = 1
        visited = set()
        queue = deque()
        
        visited.add((0,0))
        queue.append((0,0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == (rows - 1) and c == (cols - 1):
                    return length
                
                directions = [[0,1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visited or grid[row][col] == 1:
                        continue
                    else:
                        queue.append((row,col))
                        visited.add((row,col))
                
            length += 1
        
        return -1
                    



            

            
