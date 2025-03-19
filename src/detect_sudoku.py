import cv2
import numpy as np
import os
import shutil
import json  # Add import for JSON

def detect_sudoku_grid(image_path, output_folder='data/sudoku_squares', debug_enabled=False):
    # Delete output folder if it exists
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

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

    # Use the largest contour as the whole grid
    grid_contour = contours[0]
    peri = cv2.arcLength(grid_contour, True)
    approx = cv2.approxPolyDP(grid_contour, 0.02 * peri, True)
    if len(approx) == 4:
        # Warp the grid into a square
        pts = approx.reshape(4, 2)
        rect = np.zeros((4, 2), dtype="float32")

        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]

        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]

        (tl, tr, br, bl) = rect
        maxWidth = max(int(np.linalg.norm(br - bl)), int(np.linalg.norm(tr - tl)))
        maxHeight = max(int(np.linalg.norm(tr - br)), int(np.linalg.norm(tl - bl)))

        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype="float32")

        M = cv2.getPerspectiveTransform(rect, dst)
        grid = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

        if debug_enabled:
            cv2.imshow("Warped Grid", grid)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # Convert the grid to grayscale and find the interior contours
        grid_gray = cv2.cvtColor(grid, cv2.COLOR_BGR2GRAY)
        grid_blurred = cv2.GaussianBlur(grid_gray, (5, 5), 0)
        grid_edged = cv2.Canny(grid_blurred, 50, 150)

        # Apply morphological operations to enhance the edges
        kernel = np.ones((3, 3), np.uint8)
        grid_edged = cv2.dilate(grid_edged, kernel, iterations=2)
        grid_edged = cv2.erode(grid_edged, kernel, iterations=2)

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

        # Sort squares by their position, accounting for grid warping
        squares.sort(key=lambda s: (round(s[1] / (grid.shape[0] // 9)), round(s[0] / (grid.shape[1] // 9))))

        # Ensure we have exactly 81 squares
        if len(squares) != 81:
            print(f"Expected 81 squares, but found {len(squares)}.")

        # Save squares in the correct order
        metadata = []  # Initialize metadata list
        for i, (gx, gy, square) in enumerate(squares):
            square = cv2.resize(square, (28, 28))
            row = i // 9
            col = i % 9
            cv2.imwrite(os.path.join(output_folder, f'square_{row}_{col}.png'), square)
            # Append metadata for each square
            metadata.append({
                'row': row,
                'col': col,
                'x': int(gx),
                'y': int(gy),
                'width': int(square.shape[1]),
                'height': int(square.shape[0])
            })

        # Save metadata to a JSON file
        with open(os.path.join(output_folder, 'metadata.json'), 'w') as f:
            json.dump(metadata, f, indent=4)

        # Compile all images into one grid for debugging
        if debug_enabled:
            grid_image = np.zeros((28 * 9, 28 * 9), dtype=np.uint8)
            for row in range(9):
                for col in range(9):
                    square_path = os.path.join(output_folder, f'square_{row}_{col}.png')
                    if os.path.exists(square_path):
                        square_img = cv2.imread(square_path, cv2.IMREAD_GRAYSCALE)
                        grid_image[row * 28:(row + 1) * 28, col * 28:(col + 1) * 28] = square_img
            cv2.imshow("Compiled Grid", grid_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return squares

    raise ValueError("Could not find a valid grid contour.")

# Example usage
if __name__ == "__main__":
    try:
        detect_sudoku_grid('sudoku.jpg', debug_enabled=True)
    except (FileNotFoundError, ValueError) as e:
        print(e)
