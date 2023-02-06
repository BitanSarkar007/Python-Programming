# Q.1) We consider the N-queens problem here. The goal of the N-queens problem is to place eight queens on a chessboard
# such that no queen attacks any other. The problem formulation in terms of the state-space is as follows:
# 1. fs: Any arrangement of 0-N queens on the board is a state.
# 2. Initial State: No queens on the board.
# 3. Actions: Add a queen to any empty square.
# 4. Transition Model: Returns the board with a queen added to the specified square.
# 5. Goal test: N queens are on the board, none attacked.
# Write a program to:
# 1. Solve the problem starting from the initial state and print the solution chessboard.
# 2. Print the number of solutions to the problem.
# 3. Print the number of non-attacking states.

all_solutions = []
treeq = []

l = []
non_attacking_states = 0
treeq.append(l)

N =int(input("Enter the number of queens: "))

def is_attacked(state, col):
    row = len(state)
    for r in range(row):
        if state[r] == col or state[r] - r == col - row or state[r] + r == col + row:
            return True
    return False


while (treeq != []):
    state = treeq.pop(0)
    if len(state) == N:
        all_solutions.append(state)
    else:
        for col in range(N):
            if not is_attacked(state, col):
                treeq.append(state + [col])
                non_attacking_states += 1


def print_board(board):
    for row in board:
        print(''.join('Q' if col == 1 else '.' for col in row))


def print_solution(solution):
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i, col in enumerate(solution):
        board[i][col] = 1
    print_board(board)

def main():
        for solution in range(len(all_solutions)):
            print_solution(all_solutions[solution])
            print(" ")
        print('Number of non attacking states: ',non_attacking_states)
        print('Number of solutions: ', len(all_solutions))


if __name__ == "__main__":
    main()
