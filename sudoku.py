import numpy as np
import sys


class Sudoku:

  def __init__(self, grid):
    self.grid = grid

  def around(self, y, x):
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
      self.grid[r][c] for r in range(coordY - 1, coordY + 2)
      for c in range(coordX - 1, coordX + 2)
      if (r >= 0 and r < len(self.grid) and c >= 0 and c < len(self.grid[0]))
    ])

  def check(self, y, x, num):
    if np.count_nonzero(self.around(y, x) == num) > 1:
      return False
    if np.count_nonzero(self.grid[0:9, x] == num) > 1 or np.count_nonzero(
        self.grid[y] == num) > 1:
      return False
    return True

  def find(self, end):
    for index, num in np.ndenumerate(self.grid):
      if num == 0:
        for i in range(1, 10):
          self.grid[index] = i
          if self.check(index[0], index[1], i):
            if index == end:
              return True
            else:
              if not self.find(end):
                continue
            break
        else:
          return False

  def solve(self, end):
    self.find(end)
    return self.grid

  def isSolved(self):
    for row in range(self.grid.shape[0]):
      for col in range(self.grid.shape[1]):
        num = self.grid[row, col]
        if not num or not self.check(col, row, num):
          return False
    return True
