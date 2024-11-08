import numpy as np
from sudoku import Sudoku
import sys

def main():
    if len(sys.argv) < 2:
        print("Using an example:\n")
        input_file = "puzzles.txt"
    else:
        print("Using input:\n")
        input_file = sys.argv[1]
    
    try:
        input_file = open(input_file, "r")
    except:
        print("Error opening file")
        return 1
    
    last = (0, 0)
    sudoku = input_file.readline().strip()
    sudoku = Sudoku(
        np.array(
            [np.array(list(map(int, sudoku[x:x + 9])))for x in range(0, 81, 9)]
        )
    )
    print("Original sudoku:\n", sudoku.grid)
    for y in range(8, -1, -1):
        for x in range(8, -1, -1):
            if sudoku.grid[y][x] == 0:
                last = (y, x)
                break
        else:
            continue
        break

    print("Is original sudoku solved? True/False\n", sudoku.isSolved())
    print("Solved sudoku:\n", sudoku.solve(last))
    print(
        "Is solved sudoku actually solved? (If not the sudoku was unsolvable): True / False:\n",
        sudoku.isSolved()
    )
    input_file.close()


if __name__ == "__main__":
  main()
  
