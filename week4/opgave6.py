import copy
#N = 9
# i is de index


def to_board(s):
    """Input is a string of space-separated rows filled with N^2 numbers.
       Result is a list of size N^2."""
    s = s.replace("\n", " ")
    return [int(x) for x in s.split()]





def display(board):
    "input is a list of integers, print the list as a board"
    for i in range(0, SIZE, N):
        s = ''
        for x in board[i:i + N]:  # extract the rows
            assert x < 100
            s = s + '{:3d}'.format(x)
        print(s)


# s = """
# 0  0  0  0  0  0  0  0 81
# 0  0 46 45  0 55 74  0  0
# 0 38  0  0 43  0  0 78  0
# 0 35  0  0  0  0  0 71  0
# 0  0 33  0  0  0 59  0  0
# 0 17  0  0  0  0  0 67  0
# 0 18  0  0 11  0  0 64  0
# 0  0 24 21  0  1  2  0  0
# 0  0  0  0  0  0  0  0  0 """

s = """
1 0 0
0 5 0
0 0 9 """

board = to_board(s)
print("the board> ", s)

SIZE = len(board)  # the total size, e.g. 81
N = int(SIZE ** 0.5)  # size of row or column, e.g. 9
# only hor & ver, no wrapping

def neighbors(i):
    result = []
    row = i // N  # [0..N-1]
    # your code
    if i > 0 and (i - 1)//N == row:
        firstNeighborIndex = i - 1
        result.append(firstNeighborIndex)

    if i < SIZE-1 and (i + 1)//N == row:
        secondNeighborIndex = i + 1
        result.append(secondNeighborIndex)

    if i > N-1:
        thirdNeighborIndex = i - N
        result.append(thirdNeighborIndex)

    if i < SIZE - N:
        fourthNeighborIndex = i + N
        result.append(fourthNeighborIndex)

    return result

#print(neighbors(0))

# extract and sort the clues
clues = sorted([int(x) for x in board if x != 0])
assert clues[0] == 1
assert clues[-1] == SIZE  # last clue must equal SIZE


# pos = index in list b, count = distance starting from 1, clue_index = index in list clues
# note : will try all paths & will find all solutions
def solve(pos, count, clueValueCounter, b):
    neighBorIndexList = neighbors(pos)

    #TODO cluevalue klopt niet dit moet verbeterd worden.
    clueValue = clues[clueValueCounter]
    tempBoard = copy.copy(b)
    if count == SIZE:
        print("done")
        print(tempBoard)
        return

    for index in neighBorIndexList:
        if tempBoard[index] == 0:
            tempBoard[index] = count
            solve(index, count+1, clueValueCounter, tempBoard)

        if tempBoard[index] != 0:
            if count == tempBoard[index]:
                solve(index, count+1, clueValueCounter, tempBoard)



pos = board.index(0)
#print(pos)
solve(0, count=2, clueValueCounter=0, b=board)
