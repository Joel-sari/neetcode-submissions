class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        #                down    right    up      left
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

         

        def dfs_capture(row, col): 
            # if we lan on an x we should be done
            if (row < 0 or col < 0 or row == ROWS or col == COLS
                or board[row][col] != "O"): 
                return

            # everything connected to the border IS NOT SURROUNDED by X's since the border would implicate an O we shouldn't touch
            board[row][col] = "T"

            for dir_x, dir_y in directions: 
                new_r, new_c = row + dir_x, col + dir_y
                dfs_capture(new_r, new_c)

        # 1. Captuer unsurrounded regions (0 -> T) (any Os in the borders)
        for r in range(ROWS): 
            for c in range(COLS): 
                # now we only want to run the algorithm on the borders and on O's 
                if (board[r][c] == "O" and
                # by using creating an array indicating row 0 and row -1,( same with cols) we get the check of whether or not we are in the borders which is what we want 
                 r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    dfs_capture(r, c)


        # Phase 2. Capture surrounded regions (0-> X) turn them into X's 

        # this is pretty straightforward, since the one's we arent supposed to flip are converted into T's we can jsust scan the matrix and convert those that are O's still to X's
        for row in range(ROWS): 
            for col in range(COLS): 
                if board[row][col] == 'O': 
                    board[row][col] = 'X'

        

        # Phase 3. we can just revert the T's into X's

        for row in range(ROWS): 
            for col in range(COLS):
                if board[row][col] == 'T': 
                        board[row][col] = 'O'

            





        