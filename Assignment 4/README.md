# Search

This program solves the N-Queens problem using the hill climbing search algorithm. The N-Queens problem involves placing N queens on an N×N chessboard such that no two queens threaten each other. A queen can move horizontally, vertically, or diagonally.

# Problem Formulation

States: An arrangement of N queens on an N×N chessboard where no two queens threaten each other is a state.
Initial State: An initial arrangement of N queens on the chessboard.
Actions: Moving one queen to another row within its column.
Transition Model: Returns the new arrangement of queens after moving one queen to another row within its column.
Goal Test: Whether the current arrangement of queens is a valid solution where no two queens threaten each other.

# How to Run the Program

1. Clone the repository or download the zip file.
2. Navigate to the directory where the files are located.
3. The program can be run using the following command:
```
python3 search.py
```
4. The program will prompt the user to enter the number of queens to be placed on the chessboard.

The program will then print the initial state, the goal state, and the solution state. The program will also print the number of steps taken to reach the solution state.

