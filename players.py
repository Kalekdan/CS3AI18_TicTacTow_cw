class Player:
    def __init__(self, val):
        self.val = val

    def makeMove(self, board):
        pass

    def getInput(self):
        pass


class HumanPlayer(Player):
    def makeMove(self, board):
        move = self.getInput()
        move_is_valid = board.isValidMove(move[0], move[1])
        while not move_is_valid:
            print("Invalid input - try again")
            move = self.getInput()
            move_is_valid = board.isValidMove(move[0], move[1])
        board.playpiece(move[0], move[1], self.val)

    def getInput(self):
        col = input("Player " + self.val + " - Enter column: ")
        row = input("Player " + self.val + " - Enter row: ")
        return int(col), int(row)
