# Q.1) We consider the 8-queens problem here. The goal of the 8-queens problem is to place eight queens on a chessboard such that no queen attacks any other. The problem formulation in terms of the state-space is as follows:
# 1. States: Any arrangement of 0-8 queens on the board is a state.
# 2. Initial State: No queens on the board.
# 3. Actions: Add a queen to any empty square.
# 4. Transition Model: Returns the board with a queen added to the specified square. 5. Goal test: 8 queens are on the board, none attacked.
# Write a program to:
# 1. Solve the problem starting from the initial state and print the solution chessboard.
# 2. Print the number of solutions to the problem.
# 3. Print the number of non-attacking states.

import time

solutions=[] # list of tuples
all_solutions=[] # list of lists of tuples

num_non_att_states = 0 

def print_board(p): 
    print('-----------------')
    for i in range(8):
      print('|', end='')
      x = p[i]
      for j in range(8):
        if x[0] == i and x[1]==j : 
            print('Q|', end='') # Q here denotes queen
        else:
            print(' |', end='')
      print(' ')
      print('-----------------')
        
def is_attacked(row, col):  
    for s in solutions: # check if the queen is attacked in the row, column or diagonal
        if s[1] == col or s[0] == row or s[1]+s[0]==col+row or s[1]-s[0]==col-row: 
            return True
    return False

def solve():
    global num_non_att_states
    c = 0 # column
    r = 1 # row
    k = 0 # counter
    solutions.append((0,0)) # initial position for the queen
    while(r!=8):
        for col in range(c,8): # check for all columns in the row
            if not is_attacked(len(solutions), col): # if not attacked, add to the list
                solutions.append((r, col)) # add the queen to the board
                num_non_att_states += 1 # increment the number of non-attacking states
                k+= 1 # increment the counter
                break;
        if len(solutions) == 8: # if 8 queens are placed, add the solution to the list of solutions
            all_solutions.append(solutions.copy()) # add the solution to the list of solutions
            k = 0 # reset the counter
        if k == 0: # if no queen is placed in the row, backtrack
            if len(solutions) == 0: # if no solution is found,
                return 
            temp = solutions.pop() # remove the last queen
            c = temp[1] + 1 # start from the next column
            r = temp[0] # start from the same row
        else:
            c = 0 # start from the first column
            r += 1 # move to the next row
            k = 0 # reset the counter

def get_solutions():
    print (all_solutions)

def get_number_of_solutions():
    return len(all_solutions)

def get_number_of_non_attacking_states():
    return num_non_att_states

def main():
    start = time.time()
    solve() # solve the problem
    end = time.time()
    print('Time taken to solve the problem: ', end-start)
    print('Number of solutions: ', get_number_of_solutions())
    print('Number of non-attacking states: ', get_number_of_non_attacking_states())
    print('Solutions: ')

    print('Solution 1: ')
    print_board(all_solutions[0])
    print('Solution 2: ')
    print_board(all_solutions[1])


if __name__ == '__main__':
    main()
