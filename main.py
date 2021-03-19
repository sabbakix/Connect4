"""
Connect 4
"""

from termcolor import colored

red = colored(u'\u2B24', 'red')
green = colored(u'\u2B24', 'green')

# inizial matrix
# 0 mean empty, 1 mean player 1, 2 mean player 2
board =  [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]


# Print board
def print_board():
    global board
    rows = len(board)
    cols = len(board[0])
    for col in range (cols):
        print(str(col+1)+" ", end="")
    print("")
    for row in range(rows):
        for col in range (cols):
            if board[row][col] == 0:
                print(" |", end="")
            if board[row][col] == 1:
                print(green+"|", end="")
            if board[row][col] == 2:
                print(red+"|", end="")
        print("")
        for col in range (cols*2):
            print("-", end="")
        print("")


# Add chip to the matrix 
def add(inputcol,player):
    global board
    rows = len(board)
    cols = len(board[0])
    addchip = True

    # scan the matrix
    for row in range(rows):
        for col in range (cols):

            # start to check empty spot from the last row and last col
            reverse_row = rows-int(row)-1
            reverse_col = cols-int(col)-1
            
            # if the space is empy, and chip not already added add
            # the chip at the bottom of the column
            if board[reverse_row][reverse_col] == 0:
                if addchip == True and inputcol-1 == reverse_col:
                    board[reverse_row][reverse_col] = player
                    addchip = False


# Print board
print_board()

while(True):

    # Ask input player1
    inputcol = input(green+" Player 1. Insert column: ")

    # If  input is empty exit the program
    if inputcol == "":
        break

    # Clear screen
    print(chr(27)+"[2J")

    # Add to matrix
    add(int(inputcol),1)

    # Print board
    print_board()

    # Ask input player2
    inputcol = input(red+" Player 2. Insert column: ")

    # If  input is empty exit the program
    if inputcol == "":
        break

    # Clear screen
    print(chr(27)+"[2J")

    # Add to matrix
    add(int(inputcol),2)

    # Print board
    print_board()