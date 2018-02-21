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


board()
opoints = 0
xpoints = 0
tie = 0
while True:
    while True:
        if tie == 9:
            print("It's a tie!")
        location = int(input("choose a location for O: "))
        tie += 1
        if A[location] == " ":
            A[location] = "O"
            break
        elif A[location] != " ":
            print("Occupied")
    board()

    for i in range(1, 8, 3):  # (Ez vizsgálja a vízszintes sorokat, hogy megvan-e a három "O".)
        if A[i] == "O" and A[i+1] == "O" and A[i+2] == "O":
            opoints += 1
            print("O is the winner!")
            print(opoints)

    for i in range(1, 4):  # (Ez vizsgálja a függőleges sorokat, hogy megvan-e a három "O".)7
        if A[i] == "O" and A[i+3] == "O" and A[i+6] == "O":
            opoints += 1
            print("O is the winner!")
            print(opoints)

    if (A[1] == "O" and A[5] == "O" and A[9] == "O"):
        opoints += 1
        print("O is the winner!")
        print(opoints)

    if (A[3] == "O" and A[5] == "O" and A[7] == "O"):
        opoints += 1
        print("O is the winner!")
        print(opoints)
#------------------------------------------------------------------------------#
    while True:
        if tie == 9:
            print("It's a tie!")
        location = int(input("choose a location for X: "))
        tie += 1
        if A[location] == " ":
            A[location] = "X"
            break
        elif A[location] != " ":
            print("Occupied")
    board()

    for i in range(1, 8, 3):  # (Ez vizsgálja a vízszintes sorokat, hogy megvan-e a három "X".)
        if A[i] == "X" and A[i+1] == "X" and A[i+2] == "X":
            xpoints += 1
            print("X is the winner!")
            print(xpoints)

    for i in range(1, 4):  # (Ez vizsgálja a vízszintes sorokat, hogy megvan-e a három "X".)
        if A[i] == "X" and A[i+3] == "X" and A[i+6] == "X":
            xpoints += 1
            print("X is the winner!")
            print(xpoints)
    if (A[1] == "X" and A[5] == "X" and A[9] == "X"):
        xpoints += 1
        print("X is the winner!")
        print(xpoints)
    if (A[3] == "X" and A[5] == "X" and A[7] == "X"):
        xpoints += 1
        print("X is the winner!")
        print(xpoints)
