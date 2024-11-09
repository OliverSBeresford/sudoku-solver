import numpy as np
from sudoku import Sudoku
import sys

def main():
    # User passed no arguments
    if len(sys.argv) < 2:
        print("Using an example:\n")
        input_file = "puzzles.txt"
    # Using the first argument (after the python file name) as input
    else:
        print("Using input:\n")
        input_file = sys.argv[1]
    
    # Opening the text file
    try:
        input_file = open(input_file, "r")
    except:
        print("Error opening file")
        return 1
    
    # Initializing last, just in case
    last = (0, 0)
    sudoku = input_file.readline().strip()
    # Initializes a Sudoku object with the grid corresponding to the first line of the input file
    sudoku = Sudoku(
        np.array(
            [np.array(list(map(int, sudoku[x:x + 9])))for x in range(0, 81, 9)]
        )
    )
    
    # Finding the last empty square of the sudoku board (see find function)
    for y in range(8, -1, -1):
        for x in range(8, -1, -1):
            if sudoku.grid[y][x] == 0:
                last = (y, x)
                break
        else:
            continue
        break
    
    # Colors needed for printing to the terminal
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m' # orange on some systems
    WHITE = '\033[97m'

    RESET = '\033[0m' # used to return to standard terminal text color
    
    print("Original sudoku:\n", sudoku.grid)
    solved = sudoku.isSolved()
    print(f"Is original sudoku solved? True / False:\n>{YELLOW if solved else WHITE} {solved}{RESET}")
    
    print(f"Solved sudoku:\n{sudoku.solve(last)}")
    solved = sudoku.isSolved()
    print(f"Was the sudoku solvable? True / False:\n>{GREEN if solved else RED} {solved}{RESET}")
    
    input_file.close()


if __name__ == "__main__":
  main()
  
