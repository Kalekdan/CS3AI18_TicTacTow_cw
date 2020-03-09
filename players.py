import copy

from gameboard import GameBoard


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

    def make_move_explicit(self, board, move):
        move_is_valid = board.isValidMove(move[0], move[1])
        while not move_is_valid:
            print("Invalid input - try again")
            return -1
        board.playpiece(move[0], move[1], self.val)

    def minimax(self, board, depth, is_maximizer):
        depth_penalty = 0
        # if is_maximizer:
        #     depth_penalty = depth
        # else:
        #     depth_penalty = -depth
        if board.check_game_won() == "X":
            # board.debugBoard()
            return -1 + depth_penalty
        if board.check_game_won() == "O":
            # board.debugBoard()
            return 1 + depth_penalty
        if not board.movesRemaining():
            # board.debugBoard()
            return 0 + depth_penalty

        if is_maximizer:
            best_val = -10000
            for cols in range(3):
                for rows in range(3):
                    if board.isValidMove(cols, rows):
                        board.playpiece(cols, rows, "O")
                        best_val = max(best_val, self.minimax(board, depth + 1, not is_maximizer))
                        board.playpiece(cols, rows, "")
            return best_val
        else:
            best_val = 10000
            for cols in range(3):
                for rows in range(3):
                    if board.isValidMove(cols, rows):
                        board.playpiece(cols, rows, "X")
                        best_val = min(best_val, self.minimax(board, depth + 1, not is_maximizer))
                        board.playpiece(cols, rows, "")
            return best_val

    def make_move_ai(self, board):
        best_move = -1, -1
        if self.val == "O":
            best_val = -1000
            for cols in range(3):
                for rows in range(3):
                    if board.isValidMove(cols, rows):
                        temp_board = GameBoard()
                        temp_board.board = copy.deepcopy(board.board)
                        temp_board.playpiece(cols, rows, self.val)
                        move_val = self.minimax(temp_board, 0, False)
                        if move_val > best_val:
                            best_val = move_val
                            best_move = cols, rows
        else:
            best_val = 1000
            for cols in range(3):
                for rows in range(3):
                    if board.isValidMove(cols, rows):
                        temp_board = GameBoard()
                        temp_board.board = copy.deepcopy(board.board)
                        temp_board.playpiece(cols, rows, self.val)
                        move_val = self.minimax(temp_board, 0, True)
                        if move_val < best_val:
                            best_val = move_val
                            best_move = cols, rows
        print("Player " + self.val + ": Minimax Score = " + str(best_val) + " - Optimal move = " + str(best_move))
        board.playpiece(best_move[0], best_move[1], self.val)

    def getInput(self):
        col = input("Player " + self.val + " - Enter column: ")
        row = input("Player " + self.val + " - Enter row: ")
        return int(col), int(row)
