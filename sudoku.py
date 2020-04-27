import random
import time

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

def printboard():
    for i in board:
        print(i)

def find_empty_location():
    for row in range(0,9):
        for column in range(0,9):
            if board[row][column]==0:
                return (row,column)
    return (-1,-1)

def checkfit(row,column,x):
    #check row
    if x in board[row]:
        return False
    #check column
    for i in range(0,9):
        if board[i][column]==x:
            return False
    #check sub-grid
    row_start = (row//3)*3
    col_start = (column//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[row_start+i][col_start+j] == x:
                return False
    return True


def solver(app):
        row, column = find_empty_location()
        if row==-1:
            return True
        for x in range(1,10):
            if checkfit(row,column,x):
                board[row][column]=x
                app.update(reset=False,latest=[row,column])
                time.sleep(0.02)
                if(solver(app)):
                    return True
                board[row][column]=0
        return False

def solver_for_init():
    row, column = find_empty_location()
    if row==-1:
        return True
    for x in range(1,10):
        if checkfit(row,column,x):
            board[row][column]=x
            if(solver_for_init()):
                return True
            board[row][column]=0
    return False

def init_board():
    #reset the board to zero
    for i in range(0,9):
        for j in range(0,9):
            board[i][j] = 0
    
    #Get a random solved board
    random_row = [1,2,3,4,5,6,7,8,9]
    random.shuffle(random_row)
    board[0] = random_row
    solver_for_init()

    #randomly remove elements
    for i in range(0,120):
        a = random.randrange(0,9)
        b = random.randrange(0,9)
        board[a][b] = 0


