import numpy as np
import sys

def around(grid, x, y):
  return np.array([
    grid[r][c] for r in range(y - 1, y + 2) for c in range(x - 1, x + 2)
    if (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])
        and grid[r][c] != grid[y][x])
  ])

def check(grid, x, y, num):
  if num in around(grid, y, x):
    return False
  elif np.count_nonzero(grid[0:9, x] == num) >= 2 or np.count_nonzero(grid[y] == num) >= 2:
    return False
  return True


def find(g, end):
  for num in np.nditer(g, flags=["multi_index"]):
    if not num:
      for i in range(1, 10):
        if check(g, num.multi_index[1], num.multi_index[0]):
          g[num.multi_index] = i
          if num.multi_index == end:
            return True
          else:
            if not find(g, end):
              continue
          break
      else:
        return False


def solve(sudokuBoard, end):
  find(sudokuBoard, end)
  return

def isSolved(sud):
    for row in range(sud.shape[0]):
        for col in range(sud.shape[1]):
            num = sud[row, col]
            print(f"Element at ({row}, {col}): {num}")
            if not check(sud, col, row, num):
                return False
    return True


def main():
  f = open("0.txt")
  last = (0, 0)
  sudoku = f.readline().strip()
  sudoku = np.array(
    [np.array(list(map(int, sudoku[x:x + 9]))) for x in range(0, 81, 9)])
  print(sudoku)
  for y in range(8, -1, -1):
    for x in range(8, -1, -1):
      if not sudoku[y][x]:
        last = (y, x)
        break
    else:
      continue
    break
  print(sudoku.dtype, sudoku.shape)
  print(isSolved(sudoku))
  f.close()


if __name__ == "__main__":
  main()
