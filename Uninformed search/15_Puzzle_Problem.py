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

openList = []
closedList = []
pos = None
path = []
parent = {}

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
    temp_pos = pos[0] - 1, pos[1]
    if check(temp_pos):
        return True
    else:
        return False

def bottom(pos):
    temp_pos = pos[0] + 1, pos[1]
    if check(temp_pos):
        return True
    else:
        return False

def left(pos):
    temp_pos = pos[0], pos[1] - 1
    if check(temp_pos):
        return True
    else:
        return False

def right(pos):
    temp_pos = pos[0], pos[1] + 1
    if check(temp_pos):
        return True
    else:
        return False


def move(board, path):
    if left(pos):
        temp_board = copy.deepcopy(board)
        temp_board[pos[0]][pos[1]] = board[pos[0]][pos[1]-1]
        temp_board[pos[0]][pos[1]-1] = 0
        if temp_board not in closedList:
            openList.append(temp_board)
            parent[str(temp_board)] = [board, "left"]
            path.append("left")
    if right(pos):
        temp_board = copy.deepcopy(board)
        temp_board[pos[0]][pos[1]] = board[pos[0]][pos[1]+1]
        temp_board[pos[0]][pos[1]+1] = 0
        if temp_board not in closedList:
            openList.append(temp_board)
            parent[str(temp_board)] = [board, "right"]
            path.append("right")
    if top(pos):
        temp_board = copy.deepcopy(board)
        temp_board[pos[0]][pos[1]] = board[pos[0]-1][pos[1]]
        temp_board[pos[0]-1][pos[1]] = 0
        if temp_board not in closedList:
            openList.append(temp_board)
            parent[str(temp_board)] = [board, "top"]
            path.append("top")
    if bottom(pos):
        temp_board = copy.deepcopy(board)
        temp_board[pos[0]][pos[1]] = board[pos[0]+1][pos[1]]
        temp_board[pos[0]+1][pos[1]] = 0
        if temp_board not in closedList:
            openList.append(temp_board)
            parent[str(temp_board)] = [board, "bottom"]
            path.append("bottom")
            
def goal(board, goal_board):
    if board == goal_board:
        return True
    else:
        return False

def graph_search(board, goal_board):
    openList.append(board)
    while openList:
        board = openList.pop(0)
        closedList.append(board)
        global pos
        pos = blank(board)
        if goal(board, goal_board):
            print("Goal Reached")
            # print(board)
            # print(path)
            break
        move(board, path)
def trace_path(board, current_board):
    # print(current_board) 
    if board == current_board:
        return True
    else:
        print(parent[str(current_board)][1])
        current_board=parent[str(current_board)][0]
        trace_path(board, current_board)
def main():
    print("Enter initial board configuration:")
    board = []
    for _ in range(4):
        row = input().split()
        row = [int(x) for x in row]
        board.append(row)

    print("Enter goal board configuration:")
    goal_board = []
    for _ in range(4):
        row = input().split()
        row = [int(x) for x in row]
        goal_board.append(row)

    graph_search(board, goal_board)
    trace_path(board, goal_board)

if __name__ == "__main__":
    main()
