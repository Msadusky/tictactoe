import random

def winCheck(board):
    val = []

    for y in range(len(board)):
        # Checks columns for win conditions
        for x in board:
            val.append(x[y])
        if val[0] == 1 and val[1] == 1 and val[2] == 1:
            print("Player wins!")
            break
        elif val[0] == 2 and val[1] == 2 and val[2] == 2:
            print("Computer wins!")
            break
        val.clear()

        # Checks rows for win conditions
        for x in board[y]:
            val.append(x)
        if val[0] == 1 and val[1] == 1 and val[2] == 1:
            print("Player wins!")
            break
        elif val[0] == 2 and val[1] == 2 and val[2] == 2:
            print("Computer wins!")
            break
        val.clear()

    # Checks for diagonal win condition
    if board[1][1] == 1:
        if board[0][0] == 1 and board[2][2] == 1:
            print("Player wins diag!")
        elif board[2][0] == 1 and board[0][2] == 1:
            print("Player wins diag!")

    if board[1][1] == 2:
        if board[0][0] == 2 and board[2][2] == 2:
            print("Computer wins diag!")
        elif board[2][0] == 2 and board[0][2] == 2:
            print("Computer wins diag!")

# Just in case random number generator
def randomNumbers():
    column = random.randint(1, 4)
    row = random.randint(1, 4)
    return (column, row)

# Prints the board
def printBoard(board):
    print(len(board))
    print("\n")
    for y in range(len(board)):
        for x in board:
            print(x[y], end = "")
        print("")
    print("\n")

# player's turn input
def player():
    print("Enter the X coordinate of your play then press return:")
    column = input()
    column = int(column)

    # Subtracts one from the value stay within array bounds
    column -= 1

    print("Enter the Y coordinate of your play then press return:")
    row = input()
    # Converts string to int
    row = int(row)
    row -= 1
    return (column, row)

# CPU logic goes here
def cpu(board):
    return

gameOver = False
turn = 1                # 1 = player's turn, 2 = cpu's turn

# Matrix to create on screen print out
board = [[0, 0, 2], [0, 2, 0], [2, 1, 0]]
printBoard(board)       # Prints empty board


while gameOver == False:
    if turn == 1:
        column, row = player()
        if board[column][row] == 0:
            # Each row contains an array of column values
            # Player's mark on the board is signified as 1
            # AI is signified as 2
            board[column][row] = 1
            printBoard(board)
            turn = 2
        else:
            print("Someone already played there!")
    if turn == 2:

        gameOver = True
        # CPU logic here
    winCheck(board)

print("Game exited successfully")
