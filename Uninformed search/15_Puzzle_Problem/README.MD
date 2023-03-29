# 15-Puzzle Problem Solver

This program solves the 15-puzzle problem using graph search algorithm. Given an initial board configuration and a goal board configuration, the program finds a sequence of moves that takes the initial board configuration to the goal board configuration.

# Problem Formulation

States: Any arrangement of numbers 1-15 on the board together with a blank cell is a state.
Initial State: A random placement of numbers 1-15 and the blank in the 15 cells of the board.
Actions: up, down, left, right. The respective action swaps the number to the up, down, left, right of the blank cell with the blank cell.
Transition Model: Returns the new board after an application of the action.
Goal Test: Whether the current state matches with the goal configuration.


# How to Run the Program

1. Clone the repository or download the zip file.
2. Navigate to the project directory using the terminal/command prompt.
3. Run the following command: python 15_puzzle.py
4. Input the initial board configuration by entering 4 rows of 4 numbers separated by spaces. For the blank cell, use 0.
5. Input the goal board configuration by entering 4 rows of 4 numbers separated by spaces. For the blank cell, use 0.
6. The program will output the sequence of moves that takes the initial board configuration to the goal board configuration.
