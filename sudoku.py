import numpy as np
import sys


class Sudoku:

  def __init__(self, grid):
    self.grid = grid

  def around(self, grid, y, x):
    coordX, coordY = x / 3, y / 3
    if coordX > 2:
      coordX = 7
      if coordY > 2:
        coordY = 7
      elif coordY > 1:
        coordY = 4
      else:
        coordY = 1
    elif coordX > 1:
      coordX = 4
      if coordY > 2:
        coordY = 7
      elif coordY > 1:
        coordY = 4
      else:
        coordY = 1
    else:
      coordX = 1
      if coordY > 2:
        coordY = 7
      elif coordY > 1:
        coordY = 4
      else:
        coordY = 1
    return np.array([
      grid[r][c] for r in range(coordY - 1, coordY + 2)
      for c in range(coordX - 1, coordX + 2)
      if (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]))
    ])

  def check(self, x, y, num):
    if np.count_nonzero(self.around(self.grid, y, x) == num) > 1:
      print("around")
      return False
    if np.count_nonzero(self.grid[0:9, x] == num) > 1 or np.count_nonzero(
        self.grid[y] == num) > 1:
      print("row")
      return False
    return True

  def find(self, end):
    for num in np.nditer(self.grid, flags=["multi_index"]):
      if not num:
        for i in range(1, 10):
          if self.check(self.grid, num.multi_index[1], num.multi_index[0], i):
            self.grid[num.multi_index] = i
            if num.multi_index == end:
              return True
            else:
              if not self.find(self.grid, end):
                continue
            break
        else:
          return False

  def solve(self, end):
    self.find(end)
    return

  def isSolved(self):
    for row in range(self.grid.shape[0]):
      for col in range(self.grid.shape[1]):
        num = self.grid[row, col]
        if not num or not self.check(col, row, num):
          return False
    return True
