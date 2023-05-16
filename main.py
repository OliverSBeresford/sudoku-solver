import numpy as np
from sudoku import Sudoku

def main():
  f = open("0.txt")
  last = (0, 0)
  sudoku = f.readline().strip()
  sudoku = Sudoku(np.array(
    [np.array(list(map(int, sudoku[x:x + 9]))) for x in range(0, 81, 9)]))
  print("Original sudoku:\n", sudoku.grid)
  for y in range(8, -1, -1):
    for x in range(8, -1, -1):
      if not sudoku.grid[y][x]:
        last = (y, x)
        break
    else:
      continue
    break
  print("Is original sudoku solved? True/False\n", sudoku.isSolved())
  print("Solved sudoku:\n", sudoku.solve(last))
  print(
    "Is solved sudoku actually solved? (If not the sudoku was unsolvable): True / False:\n",
    sudoku.isSolved())
  f.close()


if __name__ == "__main__":
  main()
