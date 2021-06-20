def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j == 0 :
                print(" ", end="")
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
                
def check_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def verify_row(board, value, row, column):
    for i in range(len(board)):
        if board[i][column] == value and row != i:
            return False
    return True

def verify_column(board, value, row, column):
    for i in range(len(board[0])):
        if board[row][i] == value and column != i:
            return False
    return True

def verify_subgrid(board, value, row, column):
    rows = row // 3
    columns = column // 3
    for i in range(rows*3 , rows*3+3):
        for j in range(columns*3 , columns*3+3):
            if board[i][j] == value and (i,j) != (row,column):
                return False
    return True

def verify_value(board, value, row, column):
    if verify_row(board, value, row, column) and verify_column(board, value, row, column) and verify_subgrid(board, value, row, column):
        return True
    return False
    
def verify_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True
    
def solve_sudoku(board):
    position = check_empty(board)
    if position is None:
        return True
    else:
        for i in range(1,10):
            if verify_value(board, i, position[0], position[1]):
                board[position[0], position[1]] = i
                if solve_sudoku(board):
                    return True
                board[position[0], position[1]] = 0
        return False