# Q.1) We consider the 8-queens problem here. The goal of the 8-queens problem is to place eight queens on a chessboard such that no queen attacks any other. The problem formulation in terms of the state-space is as follows:
# 1. States: Any arrangement of 0-8 queens on the board is a state.
# 2. Initial State: No queens on the board.
# 3. Actions: Add a queen to any empty square.
# 4. Transition Model: Returns the board with a queen added to the specified square. 5. Goal test: 8 queens are on the board, none attacked.
# Write a program to:
# 1. Solve the problem starting from the initial state and print the solution chessboard.
# 2. Print the number of solutions to the problem.
# 3. Print the number of non-attacking states.

import numpy as np
import time


class NQueens:

        def __init__(self, n):
            self.n = n # number of queens
            self.board = np.zeros((n, n), dtype=int)
            self.solutions = []
    
        def is_attacked(self, row, col):
            # check if the queen is attacked in the row
            for i in range(self.n):
                if self.board[row][i] == 1:
                    return True
    
            # check if the queen is attacked in the column
            for i in range(self.n):
                if self.board[i][col] == 1:
                    return True
    
            # check if the queen is attacked in the diagonal
            for i in range(self.n):
                for j in range(self.n):
                    if (i + j == row + col) or (i - j == row - col):
                        if self.board[i][j] == 1:
                            return True
            return False
    
        def solve(self, row):
            if row == self.n: # if all queens placed, return True
                # print(self.board)
                self.solutions.append(self.board.copy())
                return
    
            for col in range(self.n):
                if not self.is_attacked(row, col):
                    self.board[row][col] = 1
                    self.solve(row + 1)
                    self.board[row][col] = 0
    
        def get_solutions(self):
            return self.solutions # returns a list of solutions
    
        def get_number_of_solutions(self):
            return len(self.solutions) # returns the number of solutions
    
        def get_number_of_non_attacking_states(self):
            return self.n ** self.n # returns the number of non-attacking states

def main():
    n = 8
    n_queens = NQueens(n)
    start_time = time.time()
    n_queens.solve(0)
    print("Time taken: ", time.time() - start_time) # prints the time taken to solve the problem
    print("Number of solutions: ", n_queens.get_number_of_solutions()) # prints the number of solutions
    print("Number of non-attacking states: ", n_queens.get_number_of_non_attacking_states()) # prints the number of non-attacking states
    print('One of the solutions:')
    print(n_queens.get_solutions()[0]) # prints one of the solutions

if __name__ == "__main__":
    main()

