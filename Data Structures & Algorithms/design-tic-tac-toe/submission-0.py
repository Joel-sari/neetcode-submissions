class TicTacToe:
    """
    Algorithm/ idea behind it, we want to make it so X = -1 and X = 1, the absolute value of their addition
    should equal 3 in order for it to count as a win/complete row
    
    """

    def __init__(self, n: int):
        # This is what will hold the sum of each row!, remmeber once the row equals n, 
        # we have a winner!
        self.rows = defaultdict(int)

        # This is what will hold the sum of each column!, remmeber once the row equals n, 
        # we have a winner!
        self.columns = defaultdict(int)


        self.left_diagonal = 0

        self.right_diagonal = 0
        self.n = n 
        self.board = [[0] * n for rows in range(n)]

    """
    Def move is something called multiple times by the programmer/user
    so don't worry about looping throught
    """


    def move(self, row: int, col: int, player: int) -> int:

        # We need to check first what player we are on 
        number = 0 # here we are just initializing 

        # We change the number based on what player we have (player 1 = -1, the other player = 1)
        number = -1 if player == 1 else 1 

        


        # NOTE: you are given where in the matrix  (rows and col is passed on!)
        self.rows[row] += number
        self.columns[col] += number 

        # NOW WE NEED TO CHECK THE DIAGONALS!! How??

        # the right diagonal is checked by if row and columns are equal to eachother!
        if row == col:
            self.right_diagonal += number

        # We know that the position is a LEFT DIAGONAl if both the addition of row and column is equal t
        # exactly to n - 1 ( n is basically the dimension of the matrix)
        if row + col == self.n - 1:
            self.left_diagonal += number 

        # Lastly we need to check to see if the ABS value = n? 
        # As soon as one of our checks comes True, we immediately 
        # know that the player inserted for the move function won

        # we can use the max function to get ONE value of the multiple ways the player can win 
        if max(abs(self.rows[row]), abs(self.columns[col]), abs(self.right_diagonal), abs(self.left_diagonal)) == self.n:
            return player 

        return 0 


        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
