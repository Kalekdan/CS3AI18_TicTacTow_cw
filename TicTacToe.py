from gameboard import gameboard
from players import HumanPlayer
from tkinter import *
from tkinter import ttk


continuePlaying = False
window = Tk()
window.title("Tic Tac Toe Game")

mainframe = ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.mainloop()

while True:
    board = gameboard()
    human1 = HumanPlayer("x")
    human2 = HumanPlayer("o")

    while True:
        human1.makeMove(board)
        board.displayBoard()
        winner = board.checkgamewon()
        if winner != "":
            break

        human2.makeMove(board)
        board.displayBoard()
        winner = board.checkgamewon()
        if winner != "":
            break

    print(winner + " wins")
    if not continuePlaying:
        break
