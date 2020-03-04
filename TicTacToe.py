from gameboard import gameboard
from players import HumanPlayer
from tkinter import *
from tkinter import ttk

continuePlaying = False


class mainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self.grid()
        self.boardButtons = [[None, None, None],
                             [None, None, None],
                             [None, None, None]]
        for cols in range(3):
            for rows in range(3):
                self.boardButtons[cols][rows] = Button(self, width=10, height=5)
                self.boardButtons[cols][rows].grid(row=rows, column=cols + 1, columnspan=1)
        cls = Button(self, text="Start Game")
        cls.grid(row=1, column=0)

    def updateButtons(self, boardarr):
        for cols in range(3):
            for rows in range(3):
                self.boardButtons[cols][rows].config(text=boardarr[cols][rows])
        # self.update_idletasks()
        # self.update()


window = mainWindow()
while True:
    board = gameboard()
    human1 = HumanPlayer("x")
    human2 = HumanPlayer("o")

    while True:
        human1.makeMove(board)
        board.displayBoard(window)
        winner = board.checkgamewon()
        if winner != "":
            break

        human2.makeMove(board)
        board.displayBoard(window)
        winner = board.checkgamewon()
        if winner != "":
            break

    print(winner + " wins")
    if not continuePlaying:
        break

window.mainloop()