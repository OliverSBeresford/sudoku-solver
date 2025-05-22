import numpy as np
from sudoku import Sudoku
import sys
from interface import Interface
from detect_sudoku import detect_sudoku_grid
from detect_grid import load_and_predict_squares
from type_sudoku import move_and_type_sudoku
import argparse

def main():
    parser = argparse.ArgumentParser(description='Sudoku Solver')
    parser.add_argument('input', nargs='?', default=None, help='Input file for the sudoku')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('-t', '--type', type=int, default=3, help='Wait time before typing the sudoku')
    parser.add_argument('-m', '--dark', action='store_true', help='Enable dark mode for the sudoku grid')
    
    args = parser.parse_args()
    
    if args.input is None:
        print("Using input:\n")
        interface = Interface(9, 600, 600)
        sudoku_grid = interface.get_board()
    else:
        print("Using argument:\n")
        detect_sudoku_grid(args.input, debug_enabled=args.debug, dark_mode=args.dark)
        sudoku_grid = load_and_predict_squares("./data/sudoku_squares", debug_enabled=args.debug)
        
        # Initializing last, just in case
        last = (0, 0)
        
    # Initializes a Sudoku object with the grid corresponding to the first line of the input file
    sudoku = Sudoku(sudoku_grid)
    
    # Finding the last empty square of the sudoku board (see find function)
    last = tuple(np.argwhere(sudoku.grid == 0)[-1])
    print(f"Last empty square: {last}")
    
    # Colors needed for printing to the terminal
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m' # orange on some systems
    WHITE = '\033[97m'

    RESET = '\033[0m' # used to return to standard terminal text color
    
    # Print the original sudoku board and check if it is solved
    print("Original sudoku:\n", sudoku.grid)
    solved = sudoku.isSolved()
    print(f"Is original sudoku solved? True / False:\n>{YELLOW if solved else WHITE} {solved}{RESET}")
    
    # Solve the sudoku and check if it is solvable
    print(f"Solved sudoku:\n{sudoku.solve(last)}")
    solved = sudoku.isSolved()
    print(f"Was the sudoku solvable? True / False:\n>{GREEN if solved else RED} {solved}{RESET}")
    
    # Export solved sudoku grid to numpy array
    np.save('data/solved_sudoku.npy', sudoku.grid)
    
    # Show the sudoku board using the Interface class
    interface = Interface(9, 600, 600)
    sudoku_grid = interface.show_board(sudoku.grid)
    
    # Move and type the sudoku using arrow keys and pyautogui
    if args.type is not None and solved:
        move_and_type_sudoku('data/solved_sudoku.npy', wait_time=args.type)

if __name__ == "__main__":
    main()

