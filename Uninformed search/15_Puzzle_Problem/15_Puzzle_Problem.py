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
from collections import deque

# Find the position of the blank tile (the tile with a value of 0)
def find_blank(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j
    # If the blank tile is not found, return None
    return None

# Check if a given position is within the bounds of the 4x4 grid
def check_position(pos):
    return 0 <= pos[0] <= 3 and 0 <= pos[1] <= 3

# Calculate the Manhattan distance between two 4x4 grids
def calculate_distance(board, goal_board):
    distance = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                goal_pos = [(index // 4, index % 4) for index, value in enumerate(sum(goal_board, [])) if value == board[i][j]][0]
                distance += abs(goal_pos[0] - i) + abs(goal_pos[1] - j)
    return distance

# Get the possible moves from a given position
def get_moves(pos):
    moves = []
    directions = [("right", (0, 1)), ("left", (0, -1)), ("bottom", (1, 0)), ("top", (-1, 0))]

    for move, direction in directions:
        new_pos = pos[0] + direction[0], pos[1] + direction[1]
        if check_position(new_pos):
            moves.append((move, new_pos))

    return moves

# Move the blank tile to a new position
def move_blank(board, pos, new_pos):
    new_board = copy.deepcopy(board)
    new_board[pos[0]][pos[1]] = new_board[new_pos[0]][new_pos[1]]
    new_board[new_pos[0]][new_pos[1]] = 0
    return new_board

# Check if the current board matches the goal board
def goal_reached(board, goal_board):
    return board == goal_board

# Perform BFS on the puzzle using a modified algorithm
def bfs_modified(board, goal_board):
    open_list = deque([(board, 0)])  # Store the heuristic distance along with the board
    visited = set()
    parent = {}
    path = []

    while open_list:
        current_board, distance = open_list.popleft()
        visited.add(str(current_board))

        if goal_reached(current_board, goal_board):
            while current_board != board:
                current_board, move = parent[str(current_board)]
                path.append(move)
            return list(reversed(path))

        pos = find_blank(current_board)
        for move, new_pos in get_moves(pos):
            new_board = move_blank(current_board, pos, new_pos)
            if str(new_board) not in visited:
                new_distance = calculate_distance(new_board, goal_board)
                open_list.append((new_board, new_distance))
                open_list = deque(sorted(open_list, key=lambda x: x[1]))  # Sort based on heuristic distance
                visited.add(str(new_board))
                parent[str(new_board)] = (current_board, move)

    # If there is no solution, return None
    return None

# Main function
def main():
    # Prompt the user to enter the initial and goal board configurations
    print("Enter the initial board configuration (use 0 for the blank tile):")
    board = []
    for i in range(4):
        row = input().split()
        board.append([int(x) for x in row])

    print("Enter the goal board configuration (use 0 for the blank tile):")
    goal_board = []
    for i in range(4):
        row = input().split()
        goal_board.append([int(x) for x in row])

    # Solve the puzzle using BFS
    path = bfs_modified(board, goal_board)
    if path is None:
        print("No solution")
    else:
        # Print the solution
        print("Solution:")
        for step, move in enumerate(path, start=1):
            print(f"Step {step}: {move}")
        print(f"Number of steps: {len(path)}")

if __name__ == "__main__":
    main()
