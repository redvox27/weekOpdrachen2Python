from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4
#initializing board
board = []
for x in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)

def print_board(board):
    for row in board:
        print (" ".join(row))

#start the game and printing the board
print ("Let's play Battleship!")
print_board(board)

#define where the ship is
ship_row = randint(0, BOARD_SIZE-1)
ship_col = randint(0, BOARD_SIZE-1)

print(ship_row)
print(ship_col)
"""
here your code :
-ask the user for a guess
-if the user's right, the game ends
-warn if the guess is out of the board
-warn if the guess was already made
-if the guess is wrong, mark the point with an X and start again
-print turn and board again here
"""

finished = False
i = 1
while i <= NR_GUESSES:
    print("Turn: ", i)
    rowGuess = int(input("guess the row"))
    columnGuess = int(input("guess the column"))

    if rowGuess > 3:
        print("number out of range")
        continue

    elif columnGuess > 3:
        print("numer out of range")
        continue

    elif board[rowGuess][columnGuess] == "X":
        print("spot already guessed try again")
        continue
    else:

        if ship_row == rowGuess and ship_col == columnGuess:
            print("boom")
            break

        else:
            board[rowGuess][columnGuess] = "X"

    print_board(board)

    i += 1

if i == NR_GUESSES +1 :
    print("Game Over: Out of guesses")