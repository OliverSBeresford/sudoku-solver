import pygame
import numpy as np

class Interface:
    def __init__(self, grid_size, height, width):
        self.grid_size = grid_size
        self.height = height
        self.width = width
        self.cell_size =  width // self.grid_size
    
    def get_board(self):
        pygame.init()

        # Colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        gray = (200, 200, 200)
        blue = (0, 0, 255)

        # Create the screen
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Solver")

        # Initialize the Sudoku grid
        sudoku_grid = np.zeros((9, 9), dtype=int)

        # Function to draw the Sudoku grid
        def draw_grid():
            for i in range(self.grid_size + 1):
                if i % 3 == 0:
                    line_width = 3
                else:
                    line_width = 1
                pygame.draw.line(screen, black, (i * self.cell_size, 0), (i * self.cell_size, self.height), line_width)
                pygame.draw.line(screen, black, (0, i * self.cell_size), (self.width, i * self.cell_size), line_width)

        # Function to draw numbers on the grid
        def draw_numbers():
            font = pygame.font.Font(None, 36)
            for row in range(self.grid_size):
                for col in range(self.grid_size):
                    if sudoku_grid[row][col] != 0:
                        text = font.render(str(sudoku_grid[row][col]), True, black)
                        text_rect = text.get_rect(center=(col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2))
                        screen.blit(text, text_rect)

        # Function to highlight the selected cell
        def highlight_cell(row, col):
            pygame.draw.rect(screen, blue, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size), 2)

        clock = pygame.time.Clock()

        # Main game loop
        running = True
        selected_cell = None
        while running:
            # Cap the frame rate to 60 FPS
            dt = clock.tick(60)
            row = col = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // self.cell_size, x // self.cell_size
                    selected_cell = (row, col)
                elif event.type == pygame.KEYDOWN:
                    if selected_cell is not None and event.key >= pygame.K_1 and event.key <= pygame.K_9:
                        row, col = selected_cell
                        sudoku_grid[row][col] = event.key - pygame.K_0
                    elif event.key == pygame.K_TAB:
                        if row < 9:
                            col += 1
                        elif col < 9:
                            row += 1
                            col = 0
                        selected_cell = (row, col)

            screen.fill(white)
            draw_grid()
            draw_numbers()
            if selected_cell:
                highlight_cell(*selected_cell)
            pygame.display.flip()

        pygame.quit()

        # Return the final Sudoku grid as a NumPy array
        return sudoku_grid
    
    def show_board(self, sudoku_grid):
        pygame.init()
        
        # Colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        gray = (200, 200, 200)
        blue = (0, 0, 255)

        # Create the screen
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Solver")


        # Function to draw the Sudoku grid
        def draw_grid():
            for i in range(self.grid_size + 1):
                if i % 3 == 0:
                    line_width = 3
                else:
                    line_width = 1
                pygame.draw.line(screen, black, (i * self.cell_size, 0), (i * self.cell_size, self.height), line_width)
                pygame.draw.line(screen, black, (0, i * self.cell_size), (self.width, i * self.cell_size), line_width)

        # Function to draw numbers on the grid
        def draw_numbers():
            font = pygame.font.Font(None, 36)
            for row in range(self.grid_size):
                for col in range(self.grid_size):
                    if sudoku_grid[row][col] != 0:
                        text = font.render(str(sudoku_grid[row][col]), True, black)
                        text_rect = text.get_rect(center=(col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2))
                        screen.blit(text, text_rect)

        
        clock = pygame.time.Clock()

        # Main game loop
        running = True
        selected_cell = None
        while running:
            # Cap the frame rate to 60 FPS
            dt = clock.tick(60)
            row = col = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(white)
            draw_grid()
            draw_numbers()
            pygame.display.flip()

        pygame.quit()

        # Return the final Sudoku grid as a NumPy array
        print(sudoku_grid)
