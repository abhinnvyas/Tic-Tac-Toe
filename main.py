import os

def board(board):
    """board ---- is the list of nine elements that forms that contains the X's and the O's"""
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-"*3+"|"+"-"*3+"|"+"-"*3)
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-"*3+"|"+"-"*3+"|"+"-"*3)
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("-"*3+"|"+"-"*3+"|"+"-"*3)

def take_inputs(board):
    pos = input("Choose a Position between [1-9]: ")
    pos = int(pos) if pos.isdigit() else main(board)
    if 1<=pos<=9:
        value = input("Do you want to insert X or O: ")
        value = value.upper()
        if value=="X" or value =="O":
            if board[pos-1] == " ":
                board[pos-1] = value
            else:
                print("Can't Overwrite a Value...")
                take_inputs(board)
        else:
            print("Choose either X or O.\n")
            take_inputs(board)
    else:
        print("Write an integer between 1 to 9.\n")
        take_inputs(board)

def winnner(board):
    """board ---- is the list of nine elements that forms that contains the X's and the O's"""
    won = False
    #Diagnoal checks
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("Congratulations!!! X wins")
        won = True
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("Congratulations!!! O wins")
        won = True
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("Congratulations!!! X wins")
        won = True
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("Congratulations!!! O wins")
        won = True
    #Column Checks
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("Congratulations!!! X wins")
        won = True
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("Congratulations!!! O wins")
        won = True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("Congratulations!!! X wins")
        won = True
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("Congratulations!!! O wins")
        won = True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("Congratulations!!! X wins")
        won = True
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("Congratulations!!! O wins")
        won = True
    #Row Checks
    elif board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("Congratulations!!! X wins")
        won = True
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        print("Congratulations!!! O wins")
        won = True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("Congratulations!!! X wins")
        won = True
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("Congratulations!!! O wins")
        won = True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("Congratulations!!! X wins")
        won = True
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("Congratulations!!! O wins")
        won = True

    else:
        flag = False
        ideal = []
        for i in board:
            if i == "X" or i == "O":
                flag = True
                ideal.append(flag)
            else: 
                flag = False
                ideal.append(flag)

        if ideal == [True for i in range(9)]:
            print("Game Over! Nobody Won!")
            won = True
    
    return won


def initialize(elements):
    elements = [" " for i in range(9)]
    main(elements)

def main(elements):
    os.system("cls")
    print("TIC TAC TOE | by-Abhinn Vyas")
    board(elements)
    take_inputs(elements)
    os.system("cls")
    print("TIC TAC TOE | by-Abhinn Vyas")
    board(elements)
    if winnner(elements):
        flag = input("Do you wanna play again? [Y/N]: ")
        flag = flag.lower()
        if flag == "y":
            initialize(elements)
        else:
            print("Have a Great Day!\nBye!")
            exit()
    else:
        main(elements)

if __name__ == "__main__":
        elements = []
        initialize(elements)