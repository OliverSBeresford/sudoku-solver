import cv2
import numpy as np
import os
import pytesseract

def load_and_predict_squares(squares_folder, debug_enabled=False):
    # Initialize the Sudoku grid
    sudoku_grid = np.zeros((9, 9), dtype=int)

    # Configure Tesseract to recognize only digits
    custom_config = r'--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789'

    # Iterate through the saved square images
    for i in range(81):
        square_path = os.path.join(squares_folder, f'square_{i}.png')
        if os.path.exists(square_path):
            # Load the image
            img = cv2.imread(square_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                # Use Tesseract to recognize the digit
                digit = pytesseract.image_to_string(img, config=custom_config).strip()
                if digit.isdigit():
                    sudoku_grid[i // 9, i % 9] = int(digit)
                else:
                    sudoku_grid[i // 9, i % 9] = 0

                # Debugging display
                if debug_enabled:
                    print(f"Square {i}: Recognized digit {digit}")
                    cv2.imshow(f"Square {i}", img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
            else:
                print(f"Could not read square {i}.")
        else:
            print(f"Square {i} not found.")

    return sudoku_grid

# Example usage
if __name__ == "__main__":
    squares_folder = "sudoku_squares"
    sudoku_grid = load_and_predict_squares(squares_folder, debug_enabled=True)
    print(sudoku_grid)
