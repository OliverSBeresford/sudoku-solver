import numpy as np
import pyautogui
import time

def move_and_type_sudoku(sudoku_array_path, wait_time=3):
    # Load the solved sudoku array
    sudoku_array = np.load(sudoku_array_path)
    
    # Wait for 3 seconds before starting
    time.sleep(wait_time)
    
    # Reduce the delay between key presses
    pyautogui.PAUSE = 0.01
    
    for row in range(9):
        # Alternate between moving left to right and right to left when it's even an od row respectively
        if row & 1:
            backward = True
        else:
            backward = False
        # Creating the row iterator
        row_iter = range(9) if not backward else range(8, -1, -1)
        # Going through the row
        for col in row_iter:
            # Get the digit from the solved sudoku array
            digit = sudoku_array[row, col]
            
            # Type the digit
            pyautogui.typewrite(str(digit))
            
            # Move across the row by pressing the right arrow key
            if backward:
                pyautogui.press('left')
            else:
                pyautogui.press('right')
            
        # Move to the next row
        pyautogui.press('down')

if __name__ == "__main__":
    move_and_type_sudoku('data/solved_sudoku.npy', wait_time=3)
