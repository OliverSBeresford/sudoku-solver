import numpy as np
from sudoku import Sudoku
import sys
from interface import Interface

def main():
    # User passed no arguments
    if len(sys.argv) < 2:
        print("Using input:\n")
        interface = Interface(9, 600, 600)
        sudoku_grid = interface.get_board()
    # Using the first argument (after the python file name) as input
    else:
        print("Using argument:\n")
        with open(sys.argv[1], 'r') as input_file:
            sudoku = input_file.readline().strip()
        
        # Initializing last, just in case
        last = (0, 0)
        
        sudoku_grid = np.array(
            [np.array(list(map(int, sudoku[x:x + 9])))for x in range(0, 81, 9)]
        )
    # Initializes a Sudoku object with the grid corresponding to the first line of the input file
    sudoku = Sudoku(sudoku_grid)
    
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
    
    interface = Interface(9, 600, 600)
    sudoku_grid = interface.show_board(sudoku.grid)


if __name__ == "__main__":
  main()
  
