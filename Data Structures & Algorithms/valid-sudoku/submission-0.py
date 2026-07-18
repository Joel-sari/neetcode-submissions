class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Array of strings 
        #Column, and rows must have numbers 1-9 with no duplicates

        # each 3*3 sub boxes of the grid must contain the digits 1-9 without duplicates

        cols = collections.defaultdict(set) #This another way to start a hashmap but with instatntiating it with a set value to prevent duplicates
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # they key will row/3 , column /3

        for row in range(len(board[0])):
            for col in range(len(board[0])):

                # if it's just a period we continue to the next iteration
                if board[row][col] == ".":
                    continue

                #We are checking for duplicates
                if (board[row][col] in rows[row] or 
                board[row][col] in cols[col] or
                board[row][col] in squares[(row//3, col//3)]):
                    return False

                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row //3 , col // 3)].add(board[row][col])

        return True


