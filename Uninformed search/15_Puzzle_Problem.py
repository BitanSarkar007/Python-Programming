# Q.1) We consider the 15-puzzle problem here. As an input, you will be given an initial and a goal board configuration
# and your task is to find a sequence of moves that takes the initial board configuration to the goal board configuration.
# The problem formulation in terms of the state-space
# is as follows:
# 1. States: Any arrangement of numbers 1-15 on the board together with a blank cell is a state.
# 2. Initial State: A random placement of numbers 1-15 and the blank in the 15 cells of the board.
# 3. Actions: up,down,left,right. The respective action swaps the number to the up,down,left,right of the blank cell with 
# the blank cell.
# 4. Transition Model: Returns the new board after an application of the action. Goal test: Whether the current state 
# matches with the goal configuration.
# 5. Goal test: Whether the current state matches with the goal configuration.

# Implement the graph search algorithm to print a path from the initial state leading to the goal state along with the
# corresponding action sequence (initial-board – up – next-board – down – next board – ... – right – goal-board)

openList = []
closedList = []
i =0
j = 0
pos = (i,j)

def blank(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i , j

def check(pos):
    if(pos[0] < 0 or pos[0] > 3 or pos [1] < 0 or pos[1] > 3):
        return False
    else:
        return True

def top(pos):
    temp_pos = pos[0] + 1 , pos[1]
    if check(temp_pos):
        return pos[0] + 1 , pos[1]
    else:
        return False

def bottom(pos):
    temp_pos = pos[0] - 1 , pos[1]
    if check(temp_pos):
        return pos[0] - 1 , pos[1]
    else:
        return False

def left(pos):
    temp_pos = pos[0] , pos[1] - 1
    if check(temp_pos):
        return pos[0] , pos[1] - 1
    else:
        return False

def right(pos):
    temp_pos = pos[0] , pos[1] + 1
    if check(temp_pos):
        return pos[0] , pos[1] + 1
    else:
        return False

def legal(board):
    pos = blank(board)
    row = pos[0]
    col = pos[1]
    if top(pos):
        board[row][col] = board[row-1][col]
        board[row-1][col] = 0
        openList.append(board)
    if bottom(pos):
        board[row][col] = board[row+1][col]
        board[row+1][col] = 0
        openList.append(board)
    if left(pos):
        board[row][col] = board[row][col-1]
        board[row][col-1] = 0
        openList.append(board)
    if right(pos):
        board[row][col] = board[row][col+1]
        board[row][col+1] = 0
        openList.append(board)





