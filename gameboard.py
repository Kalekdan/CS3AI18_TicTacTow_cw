class GameBoard:
    def __init__(self):
        # 3x3 Array representing the board
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]

    # return value (x or o) of winner, else empty string
    def check_game_won(self):
        # Diagonal left to right
        if (self.board[0][0] != "" and self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]):
            return self.board[0][0]
        # Diagonal right to left
        if (self.board[0][2] != "" and self.board[0][2] == self.board[1][1]) and (self.board[1][1] == self.board[2][0]):
            return self.board[0][2]
        # Horizontal top row
        if (self.board[0][0] != "" and self.board[0][0] == self.board[1][0]) and (self.board[1][0] == self.board[2][0]):
            return self.board[0][0]
        # Horizontal middle row
        if (self.board[0][1] != "" and self.board[0][1] == self.board[1][1]) and (self.board[1][1] == self.board[2][1]):
            return self.board[0][1]
        # Horizontal bottom row
        if (self.board[0][2] != "" and self.board[0][2] == self.board[1][2]) and (self.board[1][2] == self.board[2][2]):
            return self.board[0][2]
        # Vertical first column
        if (self.board[0][0] != "" and self.board[0][0] == self.board[0][1]) and (self.board[0][1] == self.board[0][2]):
            return self.board[0][0]
        # Vertical middle column
        if (self.board[1][0] != "" and self.board[1][0] == self.board[1][1]) and (self.board[1][1] == self.board[1][2]):
            return self.board[1][0]
        # Vertical last column
        if (self.board[2][0] != "" and self.board[2][0] == self.board[2][1]) and (self.board[2][1] == self.board[2][2]):
            return self.board[2][0]
        return ""

    # Update a position on the board with val
    def playpiece(self, col, row, val):
        self.board[col][row] = val

    # Update the buttons on the window to match the board object
    def displayBoard(self, window):
        window.updateButtons(self.board)

    # Print board to console
    def debugBoard(self):
        for cols in range(3):
            for rows in range(3):
                print(self.board[rows][cols], end=",\t")
            print()
        print()

    # Check that move is valid (nothing already in that space)
    def isValidMove(self, col, row):
        if self.board[col][row] == "":
            return True
        return False

    # Check if any moves remaining - if not, it is a tie
    def movesRemaining(self):
        for cols in range(3):
            for rows in range(3):
                if self.board[cols][rows] == "":
                    return True
        return False
