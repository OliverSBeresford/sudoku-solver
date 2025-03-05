import cv2
import numpy as np
import os
import shutil

def detect_sudoku_grid(image_path, output_folder='sudoku_squares', debug_enabled=False):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image file '{image_path}' not found or could not be loaded.")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)

    if debug_enabled:
        cv2.imshow("Gray", gray)
        cv2.imshow("Blurred", blurred)
        cv2.imshow("Edged", edged)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Find contours
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Delete output folder if it exists
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    # Use the largest contour as the whole grid
    grid_contour = contours[0]
    peri = cv2.arcLength(grid_contour, True)
    approx = cv2.approxPolyDP(grid_contour, 0.02 * peri, True)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        grid = image[y:y+h, x:x+w]

        if debug_enabled:
            cv2.imshow("Grid", grid)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # Convert the grid to grayscale and find the interior contours
        grid_gray = cv2.cvtColor(grid, cv2.COLOR_BGR2GRAY)
        grid_blurred = cv2.GaussianBlur(grid_gray, (5, 5), 0)
        grid_edged = cv2.Canny(grid_blurred, 50, 150)

        # Apply morphological operations to enhance the edges
        kernel = np.ones((3, 3), np.uint8)
        grid_edged = cv2.dilate(grid_edged, kernel, iterations=1)
        grid_edged = cv2.erode(grid_edged, kernel, iterations=1)

        if debug_enabled:
            cv2.imshow("Grid Gray", grid_gray)
            cv2.imshow("Grid Blurred", grid_blurred)
            cv2.imshow("Grid Edged", grid_edged)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        grid_contours, _ = cv2.findContours(grid_edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        grid_contours = sorted(grid_contours, key=cv2.contourArea, reverse=True)

        # Detect each square one at a time
        squares = []
        expected_square_area = (grid.shape[0] // 9) * (grid.shape[1] // 9)  # Expected area of each square
        min_distance = grid.shape[0] // 18  # Minimum distance between squares to consider them different
        for contour in grid_contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            if len(approx) == 4:
                gx, gy, gw, gh = cv2.boundingRect(approx)
                if 0.5 * expected_square_area < gw * gh < 1.5 * expected_square_area:  # Ensure the contour is of similar size
                    square = grid[gy:gy+gh, gx:gx+gw]
                    if all(np.linalg.norm(np.array([gx, gy]) - np.array([sx, sy])) > min_distance for sx, sy, _ in squares):
                        squares.append((gx, gy, square))

        # Sort squares by their position
        squares.sort(key=lambda s: (s[1], s[0]))

        # Ensure we have exactly 81 squares
        if len(squares) != 81:
            print(f"Expected 81 squares, but found {len(squares)}.")

        # Save squares in the correct order
        for i, (gx, gy, square) in enumerate(squares):
            cv2.imwrite(os.path.join(output_folder, f'square_{i}.png'), square)
            if debug_enabled:
                cv2.imshow(f'Square {i}', square)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        return squares

    raise ValueError("Could not find a valid grid contour.")

# Example usage
if __name__ == "__main__":
    try:
        detect_sudoku_grid('sudoku_3.jpg', debug_enabled=True)
    except (FileNotFoundError, ValueError) as e:
        print(e)
