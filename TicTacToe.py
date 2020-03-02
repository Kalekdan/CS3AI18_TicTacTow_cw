from gameboard import gameboard
from players import HumanPlayer
from tkinter import *
from tkinter import ttk

continuePlaying = False

gameWindow = Tk()
gameWindow.title("Tic Tac Toe Game")
gameWindow.grid()

ttk.Style().configure("TButton", padding=(0, 5, 0, 5),
                      font='serif 10')
gameWindow.columnconfigure(0, pad=3)
gameWindow.columnconfigure(1, pad=3)
gameWindow.columnconfigure(2, pad=3)
gameWindow.columnconfigure(3, pad=3)
gameWindow.columnconfigure(4, pad=3)

gameWindow.rowconfigure(0, pad=3)
gameWindow.rowconfigure(1, pad=3)
gameWindow.rowconfigure(2, pad=3)
gameWindow.rowconfigure(3, pad=3)
gameWindow.rowconfigure(4, pad=3)
gameWindow.rowconfigure(5, pad=3)
gameWindow.rowconfigure(6, pad=3)

boardButtons = [[None, None, None],
                [None, None, None],
                [None, None, None]]

for cols in range(3):
    for rows in range(3):
        boardButtons[cols][rows] = Button(gameWindow);
        boardButtons[cols][rows].grid(row=rows, column=cols+1, columnspan=1)

# btn = Button(gameWindow)
# btn.grid(row=0, column=1, columnspan=1)
cls = Button(gameWindow, text="Cls")
cls.grid(row=1, column=0)
bck = Button(gameWindow, text="Back")


# tk.update_idletasks()
# tk.update()
gameWindow.mainloop()

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
