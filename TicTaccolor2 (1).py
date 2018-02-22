import os
import sys

def board(A):
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



def restart_game():
    restart= input("whould you like to restart?(y/n): ")
    if restart=="y":
        main()
    if restart=="n":
        sys.exit()
        

def main():
    A = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    board(A) 
    tie=0
    O = '\033[1;32mO\033[1;m'
    X = '\033[1;34mX\033[1;m'
    end = False
    while not end:
        while True:
            if tie==9:
                print("It's a Tie!")
                end = True
                break
            location = int(input("Choose a location for O: "))
            tie+=1
            if A[location] == " ":
                A[location] = O
                break
            elif A[location] != " ":
                print("Occupied space!")
        board(A)

        for i in range(1, 8, 3):  # (Ez vizsgálja a vízszintes sorokat, hogy megvan-e a három "O".)
            if A[i] == O and A[i+1] == O and A[i+2] == O:
                end = True
                print("O won the game!")
                break

        for i in range(1, 4):  # (Ez vizsgálja a függőleges sorokat, hogy megvan-e a három "O".)7
            if A[i] == O and A[i+3] == O and A[i+6] == O:
                end = True
                print("O won the game!")
                break

        if (A[1]== O and A[5]== O and A[9]== O):
                end = True
                print("O won the game!")
                break

        if (A[3]== O and A[5]== O and A[7]== O):
                end = True
                print("O won the game!")
                break
    #------------------------------------------------------------------------------#
        while True:
            if tie==9:
                print("It's a Tie!")
                end = True
                break
            location = int(input("Choose a location for X: "))
            tie+=1
            if A[location] == " ":
                A[location] = X
                break
            elif A[location] != " ":
                print("Occupied space!")
        board(A)
        for i in range(1, 8, 3):  # (Ez vizsgálja a vízszintes sorokat, hogy megvan-e a három "X".)
            if A[i] == X and A[i+1] == X and A[i+2] == X:
                end = True
                print("X won the game!")
                break

        for i in range(1, 4):  # (Ez vizsgálja a vízszintes sorokat, hogy megvan-e a három "X".)
            if A[i] == X and A[i+3] == X and A[i+6] == X:
                end = True
                print("X won the game!")
                break

        if (A[1]== X and A[5]== X and A[9]== X):
                end = True
                print("X won the game!")
                break

        if (A[3]== X and A[5]== X and A[7]== X):
                end = True
                print("X won the game!")
                break
    if end:
        restart_game()
main()      
