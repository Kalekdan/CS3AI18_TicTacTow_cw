class Player:
    def __init__(self, val):
        self.val = val

    def makeMoveConsole(self, board):
        move = self.getInput()
        move_is_valid = board.isValidMove(move[0], move[1])
        while not move_is_valid:
            print("Invalid input - try again")
            move = self.getInput()
            move_is_valid = board.isValidMove(move[0], move[1])
        board.playpiece(move[0], move[1], self.val)

    def makeMoveExplicit(self, board, move):
        move_is_valid = board.isValidMove(move[0], move[1])
        while not move_is_valid:
            print("Invalid input - try again")
            return -1
        board.playpiece(move[0], move[1], self.val)

#TODO implement minimax
    def makeMoveAI(self, board):
        return

    def getInput(self):
        col = input("Player " + self.val + " - Enter column: ")
        row = input("Player " + self.val + " - Enter row: ")
        return int(col), int(row)

