import os
A = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def board():
    os.system('clear')

    print()
    print('   |   |   ')
    print('', A[7], '|', A[8], '|', A[9], '')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print('', A[4], '|', A[5], '|', A[6], '')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print('', A[1], '|', A[2], '|', A[3], '')
    print('   |   |   ')
    print()
tie=0

board()
#-------------------------------------------------------------
"""def restart_game(restart):
    answercontinue= input("whould you like to restart?(y/n): ")
    if restart=="y":
        restart=0
    else:
        restart=1
        print("Good bye")
        sys.exit"""
#-------------------------------------------------------------

O = '\033[1;32mO\033[1;m'
X = '\033[1;34mX\033[1;m'

while True:
    while True:
        if tie==9:
            print("It's a Tie!")
        location = int(input("Choose a location for O: "))
        tie+=1
        if A[location] == " ":
            A[location] = O
            break
        elif A[location] != " ":
            print("Occupied space!")
    board()

    for i in range(1, 8, 3):  # (Ez vizsgálja a vízszintes sorokat, hogy megvan-e a három "O".)
        if A[i] == O and A[i+1] == O and A[i+2] == O:
            print("O won the game!")

    for i in range(1, 4):  # (Ez vizsgálja a függőleges sorokat, hogy megvan-e a három "O".)7
        if A[i] == O and A[i+3] == O and A[i+6] == O:
            print("O won the game!")

    if (A[1]== O and A[5]== O and A[9]== O):
            print("O won the game!")

    if (A[3]== O and A[5]== O and A[7]== O):
            print("O won the game!")
#------------------------------------------------------------------------------#
    while True:
        if tie==9:
            print("It's a Tie!")
        location = int(input("Choose a location for X: "))
        tie+=1
        if A[location] == " ":
            A[location] = X
            break
        elif A[location] != " ":
            print("Occupied space!")
    board()
    for i in range(1, 8, 3):  # (Ez vizsgálja a vízszintes sorokat, hogy megvan-e a három "X".)
        if A[i] == X and A[i+1] == X and A[i+2] == X:
            print("X won the game!")

    for i in range(1, 4):  # (Ez vizsgálja a vízszintes sorokat, hogy megvan-e a három "X".)
        if A[i] == X and A[i+3] == X and A[i+6] == X:
            print("X won the game!")

    if (A[1]== X and A[5]== X and A[9]== X):
            print("X won the game!")

    if (A[3]== X and A[5]== X and A[7]== X):
            print("X won the game!")