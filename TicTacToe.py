from gameboard import gameboard
from players import Player
from tkinter import *
from tkinter import ttk

continuePlaying = False
currentPlayer = 0
playingVsAi = False
isGameOver = False


def togglePlayer(player):
    if player == 0:
        return 1
    return 0


def progressGame(cols, rows):
    global isGameOver
    if not isGameOver:
        global currentPlayer
        move = cols, rows
        if players[currentPlayer].makeMoveExplicit(board, move) == -1:
            print("nope")
            return
        board.displayBoard(window)
        currentPlayer = togglePlayer(currentPlayer)
        if playingVsAi:
            players[currentPlayer].makeMoveAI(board)
            currentPlayer = togglePlayer(currentPlayer)
        if board.checkgamewon():
            window.textLbl.config(text=board.checkgamewon() + " wins")
            isGameOver = True
            return
        window.textLbl.config(text=players[currentPlayer].val + "'s Turn")


class gameWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self.grid()
        self.boardButtons = [[None, None, None],
                             [None, None, None],
                             [None, None, None]]
        for cols in range(3):
            for rows in range(3):
                self.boardButtons[cols][rows] = Button(self, width=10, height=5,
                                                       command=lambda c=cols, r=rows: progressGame(c, r))
                self.boardButtons[cols][rows].grid(row=rows, column=cols + 1, columnspan=1)
        self.textLbl = Label(self, text=players[currentPlayer].val + "'s Turn")
        self.textLbl.grid(row=4, column=1, columnspan=3)

    def updateButtons(self, boardarr):
        for cols in range(3):
            for rows in range(3):
                self.boardButtons[cols][rows].config(text=boardarr[cols][rows])


board = gameboard()
human1 = Player("x")
human2 = Player("o")
players = human1, human2
window = gameWindow()
window.mainloop()

# while True:
#     board = gameboard()
#     human1 = HumanPlayer("x")
#     human2 = HumanPlayer("o")
#
#     while True:
#         human1.makeMove(board)
#         board.displayBoard(window)
#         winner = board.checkgamewon()
#         if winner != "":
#             break
#
#         human2.makeMove(board)
#         board.displayBoard(window)
#         winner = board.checkgamewon()
#         if winner != "":
#             break
#
#     print(winner + " wins")
#     if not continuePlaying:
#         break
