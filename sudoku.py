import numpy as np
import sys

class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def around(self, y, x):
        # Getting the block that it's in, from (0, 0) to (2, 2)
        coordX, coordY = x / 3, y / 3
        
        # It's in the third column
        if coordX >= 2:
            coordX = 7
            # Third row
            if coordY >= 2:
                coordY = 7
            # Second row
            elif coordY >= 1:
                coordY = 4
            # First row
            else:
                coordY = 1
        # Second column
        elif coordX >= 1:
            coordX = 4
            # Third row
            if coordY >= 2:
                coordY = 7
            # Second row
            elif coordY >= 1:
                coordY = 4
            # First row
            else:
                coordY = 1
        # First column
        else:
            coordX = 1
            # Third row
            if coordY >= 2:
                coordY = 7
            # Second row
            elif coordY >= 1:
                coordY = 4
            # First row
            else:
                coordY = 1

        # Returns a flattened array of the 8 squares surrounding the square at (x, y)        
        return np.array([
            self.grid[r][c] for r in range(coordY - 1, coordY + 2)
            for c in range(coordX - 1, coordX + 2)
        ])

    def check(self, y, x, num):
        # There is more than one occurence of num in the 9-square box
        if np.count_nonzero(self.around(y, x) == num) > 1:
            return False
        # There is more than one occurence of num in that row or column
        if np.count_nonzero(self.grid[0:9, x] == num) > 1 or np.count_nonzero(self.grid[y] == num) > 1:
            return False
        return True

    def find(self, end):
        for index, num in np.ndenumerate(self.grid):
            # For every box, if it is empty
            if num == 0:
                # Try all the numbers from 1 to 9
                for i in range(1, 10):
                    self.grid[index] = i
                    if self.check(index[0], index[1], i):
                        # If the number works, an it's the last one, we're done
                        if index == end:
                            return True
                        # If the number works, but it's not the last one, call find() for the next one
                        else:  
                            if not self.find(end):
                                # The chosen number was found to be impossible to solve with, so continue the search! (number from 1 to 9)
                                continue
                            else:
                                # Puzzle was completed, so exit the loop
                                return True
                else:
                    # Checked every number (for - else block) and they didn't work, so return false and reset square
                    self.grid[index] = 0
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