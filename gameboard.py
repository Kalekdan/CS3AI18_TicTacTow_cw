class gameboard:
    def __init__(self):
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]

#TODO add a stalemate check
    # return value (x or o) of winner, else empty string
    def checkgamewon(self):
        # Diagonal left to right
        if (self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]):
            return self.board[0][0]
        # Diagonal right to left
        if (self.board[0][2] == self.board[1][1]) and (self.board[1][1] == self.board[2][0]):
            return self.board[0][2]
        # Horizontal top row
        if (self.board[0][0] == self.board[1][0]) and (self.board[1][0] == self.board[2][0]):
            return self.board[0][0]
        # Horizontal middle row
        if (self.board[0][1] == self.board[1][1]) and (self.board[1][1] == self.board[2][1]):
            return self.board[0][1]
        # Horizontal bottom row
        if (self.board[0][2] == self.board[1][2]) and (self.board[1][2] == self.board[2][2]):
            return self.board[0][2]
        # Vertical first column
        if (self.board[0][0] == self.board[0][1]) and (self.board[0][1] == self.board[0][2]):
            return self.board[0][0]
        # Vertical middle column
        if (self.board[1][0] == self.board[1][1]) and (self.board[1][1] == self.board[1][2]):
            return self.board[1][0]
        # Vertical last column
        if (self.board[2][0] == self.board[2][1]) and (self.board[2][1] == self.board[2][2]):
            return self.board[2][0]
        return ""

    def playpiece(self, col, row, val):
        self.board[col][row] = val

    def displayBoard(self, window):
        # print(self.board[0])
        # print(self.board[1])
        # print(self.board[2])
        window.updateButtons(self.board)

    def isValidMove(self, col, row):
        if self.board[col][row] == "":
            return True
        return False
