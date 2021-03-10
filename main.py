"""
Connect 4
"""

from termcolor import colored

red = colored(u'\u2B24', 'red')
green = colored(u'\u2B24', 'green')

# inizial matrix
# 0 mean empty, 1 mean player 1, 2 mean player 2
list =  [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,1,0,0],
         [0,0,0,0,1,0,0],
         [0,0,2,1,2,0,0]]


def print_board(list):
    rows = len(list)
    cols = len(list[0])
    for col in range (cols):
        print(str(col+1)+" ", end="")
    print("")
    for row in range(rows):
        for col in range (cols):
            if list[row][col] == 0:
                print(" |", end="")
            if list[row][col] == 1:
                print(green+"|", end="")
            if list[row][col] == 2:
                print(red+"|", end="")
        print("")
        for col in range (cols*2):
            print("-", end="")
        print("")

# Print board
print_board(list)

# ask input player1 red
inputcol = input(green+" Player 1. Insert column: ")

#add to matrix


# print board

# ask input player2 green