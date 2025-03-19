import cv2
import numpy as np
import os
import pytesseract

def load_and_predict_squares(squares_folder, debug_enabled=False):
    # Initialize the Sudoku grid
    sudoku_grid = np.zeros((9, 9), dtype=int)

    # Configure Tesseract to recognize only digits
    custom_config = r'--oem 3 --psm 10 -c tessedit_char_whitelist=123456789'

    # Iterate through the saved square images
    for row in range(9):
        for col in range(9):
            square_path = os.path.join(squares_folder, f'square_{row}_{col}.png')
            if os.path.exists(square_path):
                # Load the image
                img = cv2.imread(square_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    # Use Tesseract to recognize the digit
                    digit = pytesseract.image_to_string(img, config=custom_config).strip()
                    if digit.isdigit():
                        sudoku_grid[row, col] = int(digit)
                    else:
                        sudoku_grid[row, col] = 0
                else:
                    print(f"Could not read square {row}_{col}.")
            else:
                print(f"Square {row}_{col} not found.")

    return sudoku_grid

# Example usage
if __name__ == "__main__":
    squares_folder = "..data/sudoku_squares"
    sudoku_grid = load_and_predict_squares(squares_folder, debug_enabled=False)
    print(sudoku_grid)
