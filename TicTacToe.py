from gameboard import gameboard
from players import HumanPlayer

continuePlaying = False

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
