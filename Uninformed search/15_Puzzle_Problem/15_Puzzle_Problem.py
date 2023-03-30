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
# take user input for initial and goal states
import copy

openList = [] # queue for BFS
closedList = [] # visited nodes
pos = None # position of blank
parent = {} # parent of each node
path = [] # path from initial to goal

def blank(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0: # blank is represented by 0
                return i , j

def check(pos):
    if(pos[0] < 0 or pos[0] > 3 or pos [1] < 0 or pos[1] > 3): # check if position is valid
        return False
    else:
        return True

def top(pos):
    temp_pos = pos[0] - 1, pos[1] # check if top is valid
    if check(temp_pos):
        return True
    else:
        return False

def bottom(pos):
    temp_pos = pos[0] + 1, pos[1] # check if bottom is valid
    if check(temp_pos):
        return True
    else:
        return False

def left(pos):
    temp_pos = pos[0], pos[1] - 1 # check if left is valid
    if check(temp_pos):
        return True
    else:
        return False

def right(pos):
    temp_pos = pos[0], pos[1] + 1 # check if right is valid
    if check(temp_pos):
        return True
    else:
        return False


def move(board):
    if left(pos):
        temp_board = copy.deepcopy(board)
        temp_board[pos[0]][pos[1]] = board[pos[0]][pos[1]-1]
        temp_board[pos[0]][pos[1]-1] = 0 # swap blank with left
        if temp_board not in closedList:
            openList.append(temp_board) # add to queue if not visited
            parent[str(temp_board)] = [board, "left"] # store parent of each node
            # path.append("left")
    if right(pos):
        temp_board = copy.deepcopy(board) 
        temp_board[pos[0]][pos[1]] = board[pos[0]][pos[1]+1] # swap blank with right
        temp_board[pos[0]][pos[1]+1] = 0 
        if temp_board not in closedList:
            openList.append(temp_board) 
            parent[str(temp_board)] = [board, "right"] 
            # path.append("right")
    if top(pos):
        temp_board = copy.deepcopy(board)
        temp_board[pos[0]][pos[1]] = board[pos[0]-1][pos[1]] # swap blank with top
        temp_board[pos[0]-1][pos[1]] = 0
        if temp_board not in closedList:
            openList.append(temp_board)
            parent[str(temp_board)] = [board, "top"] 
            # path.append("top")
    if bottom(pos):
        temp_board = copy.deepcopy(board)
        temp_board[pos[0]][pos[1]] = board[pos[0]+1][pos[1]] # swap blank with bottom
        temp_board[pos[0]+1][pos[1]] = 0
        if temp_board not in closedList:
            openList.append(temp_board)
            parent[str(temp_board)] = [board, "bottom"]
            # path.append("bottom")
            
def goal(board, goal_board):
    if board == goal_board:
        return True
    else:
        return False

def graph_search(board, goal_board):
    openList.append(board) # add initial board to queue
    while openList:
        board = openList.pop(0) # pop first element from queue
        closedList.append(board) # add to visited nodes
        global pos 
        pos = blank(board) # get position of blank
        if goal(board, goal_board):
            print("Goal Reached")
            # print(board)
            # print(path)
            break
        move(board) # move blank in all directions

def trace_path(board, current_board): # trace path from initial to goal
    # print(current_board) 
    if board == current_board: # if initial board is reached
        return True
    else:
        path.append(parent[str(current_board)][1]) # append action to path
        current_board=parent[str(current_board)][0] # get parent of current board
        trace_path(board, current_board) # recursively call function

def main():
    print("Enter initial board configuration:")
    board = []
    for _ in range(4):
        row = input().split() 
        row = [int(x) for x in row] # convert string to int
        board.append(row) # add row to board

    print("Enter goal board configuration:")
    goal_board = []
    for _ in range(4):
        row = input().split()
        row = [int(x) for x in row]
        goal_board.append(row)

    graph_search(board, goal_board) # perform graph search
    trace_path(board, goal_board) # trace path from initial to goal
    path.reverse() # reverse path
    for i in path:
        print(i,"->",end=" ") # print path

if __name__ == "__main__":
    main()
