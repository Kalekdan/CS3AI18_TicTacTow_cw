from tkinter import *

from gameboard import GameBoard
from players import Player

currentPlayer = 0
playingVsAi = True
isGameOver = False


def togglePlayer(player):
    if player == 0:
        return 1
    return 0


def progressGame(cols, rows):
    global currentPlayer
    if not isGameOver:
        move = cols, rows
        if players[currentPlayer].make_move_explicit(board, move) == -1:
            return
        board.displayBoard(window)
        currentPlayer = togglePlayer(currentPlayer)
    checkForGameOver()
    if playingVsAi:
        AIMove()
    checkForGameOver()


def AIMove():
    if not isGameOver:
        global currentPlayer
        players[currentPlayer].make_move_ai(board)
        board.displayBoard(window)
        checkForGameOver()
        currentPlayer = togglePlayer(currentPlayer)


def checkForGameOver():
    global isGameOver
    window.textLbl.config(text=players[currentPlayer].val + "'s Turn")
    if board.check_game_won():
        window.textLbl.config(text=board.check_game_won() + " wins")
        isGameOver = True
        return
    if not board.movesRemaining():
        window.textLbl.config(text="It's a tie!")
        isGameOver = True
        return


class GameWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self.grid()
        self.boardButtons = [[None, None, None],
                             [None, None, None],
                             [None, None, None]]
        for cols in range(3):
            for rows in range(3):
                self.boardButtons[cols][rows] = Button(self, width=3, height=1, font=("Helvetica", 45),
                                                       command=lambda c=cols, r=rows: progressGame(c, r))
                self.boardButtons[cols][rows].grid(row=rows, column=cols + 1, columnspan=1)
        self.textLbl = Label(self, text=players[currentPlayer].val + "'s Turn", font=("Helvetica", 30))
        self.textLbl.grid(row=4, column=1, columnspan=3)
        self.AIMoveBtn = Button(self, width=25, height=1, font=("Helvetica", 10),
                                command=AIMove, text="Let AI make move")
        self.AIMoveBtn.grid(row=5, column=1, columnspan=3)

    def updateButtons(self, board_arr):
        for cols in range(3):
            for rows in range(3):
                self.boardButtons[cols][rows].config(text=board_arr[cols][rows])


def startGame(menu, isVsAI):
    global playingVsAi
    playingVsAi = isVsAI
    menu.destroy()


class MenuWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.grid()
        self.startHumanVsHumanBtn = Button(self, width=25, height=1, font=("Helvetica", 20),
                                           command=lambda: startGame(self, False), text="Start Human Vs Human Game")
        self.startHumanVsHumanBtn.grid(row=2, column=1, columnspan=3)
        self.startHumanVsAIBtn = Button(self, width=25, height=1, font=("Helvetica", 20),
                                        command=lambda: startGame(self, True), text="Start Human Vs AI Game")
        self.startHumanVsAIBtn.grid(row=3, column=1, columnspan=3)


menu = MenuWindow()
menu.mainloop()
board = GameBoard()
player1 = Player("X")
player2 = Player("O")
players = player1, player2
window = GameWindow()
window.mainloop()
