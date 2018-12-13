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
print("\n")

# Matrix to create on screen print out
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Each row contains an array of column values
# Player's mark on the board is signified as 1
# AI is signified as 2
board[column][row] = 1

# Prints the matrix
for y in range(len(board)):
    for x in board:
        print(x[y], end = "")
    print("")

print("\n")
