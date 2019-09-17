def DisplayBoard(board):
    # params boards : array of array
    # boards[row][col]
    print('+', ('-' * 7 + '+') * 3, sep="")
    for row in range(0,3):
        print("|", (" " * 7 + "|") * 3, sep="")
        for col in range(0,3):
            print("|", end="")
            print(" " * 3, end="")
            print(board[row][col], end="")
            print(" " * 3, end="")
        print("|")
        print("|", (" " * 7 + "|") * 3, sep="")
        print('+', ('-' * 7 + '+') * 3, sep="")


def EnterMove(board):
    # the function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision
    valid = False
    curr_status = []
    for i in range(0,3):
        for j in range(0,3):
            curr_status.append(board[i][j])
    while not valid:
        move = input("Enter your move : ")
        if move in ["1","2","3","4","5","6","7","8","9"]:
            move = int(move)
            if curr_status[move-1] not in ["O","X"]:
                valid = True
    if move == 1:
        board[0][0] = "O"
    elif move == 2:
        board[0][1] = "O"
    elif move == 3:
        board[0][3] = "O"
    elif move == 4:
        board[1][0] = "O"
    elif move == 5:
        board[1][1] = "O"
    elif move == 6:
        board[1][2] = "O"
    elif move == 7:
        board[2][0] = "O"
    elif move == 8:
        board[2][1] = "O"
    elif move == 9:
        board[2][2] = "O"
    return board

def MakeListOfFreeFields(board):
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
    list = []
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] not in ["O","X"]:
                list.append((row,col))
    return list


def VictoryFor(board, sign):
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
    for row in range(0,3):
        if board[row][0] == board[row][1] == board[row][2]:
            print(sign, " Win!")
            return True
    for col in range(0,3):
        if board[0][col] == board[1][col] == board[2][col]:
            print(sign, " Win!")
            return True
    if board[0][0] == board[1][1] == board[2][2] or \
       board[0][2] == board[1][1] == board[2][0]:
        print(sign, " Win!")
        return True
    else:
        return False
        
    
from random import randrange       
def DrawMove(board):
    # the function draws the computer's move and updates the board
    free = MakeListOfFreeFields(board)
    move_random = free[randrange(len(free))]
    board[move_random[0]][move_random[1]] = "X"
    return board


status = [[1,2,3],[4,"X",6],[7,8,9]]
DisplayBoard(status)
menang = False
while not menang:
    status = EnterMove(status)
    DisplayBoard(status)
    menang = VictoryFor(status, "You")
    if menang:
        break
    status = DrawMove(status)
    DisplayBoard(status)
    menang = VictoryFor(status, "Computer")
 

