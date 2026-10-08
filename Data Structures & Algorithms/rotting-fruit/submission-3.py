class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minute = 0

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1

                directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                
                    if row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visited or grid[row][col] == 0:
                        continue
                    elif grid[row][col] == 1:
                        queue.append((row,col))
                        visited.add((row,col))
            minute += 1
        
        if fresh == 0:
            return minute - 1
        else:
            return -1



        

        
