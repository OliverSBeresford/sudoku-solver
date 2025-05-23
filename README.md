# Sudoku Solver
This project is a Sudoku solver that uses a backtracking algorithm to find the solution for a given Sudoku puzzle.

## Prerequisites

- Python 3.8 or above should be installed on your system (or you should be able to make a virtual environment of version 3.8 or above). If Python is not installed, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- You should probably have a version of python between 3.8 and 3.12, because 3.12 has not been tested

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/OliverSBeresford/sudoku-solver.git
   ```

2. Navigate to the project directory:
   ```shell
   cd sudoku-solver
   ```

3. Create a virtual environment:
   On macOS and Linux:
   ```shell
   python3 -m venv venv
   ```
   On Windows:
   ```shell
   py -m venv venv
   ```

4. Activate the virtual environment:
   On macOS and Linux:
   ```shell
   source venv/bin/activate
   ```
   On Windows:
   ```shell
   venv\Scripts\activate
   ```

5. Install the required packages:
   ```shell
   pip install -r requirements.txt
   ```
   This will install all the necessary dependencies for the project.

## Usage (Command Line)

To solve a Sudoku puzzle, you can provide an image of the puzzle as a command line argument. If an image is provided, the program will use it for Sudoku solving. If not, it will open an empty board and you can enter the digits with the number keys, number pad, space, tab, etc.

Example command with an image:

```shell
python3 src/main.py [image-file]
```

You can also enable debug mode, specify a wait time before typing the Sudoku, and enable dark mode using the following flags:

- `-d` or `--debug`: Enable debug mode. In debug mode, you will see images with the sudoku in each stage of the process. Click 1 to close each window.
- `-t` or `--type`: Specify the wait time before typing the Sudoku (default is 3 seconds).
- `-m` or `--dark`: Enable dark mode for the Sudoku grid.

Example command with debug mode, a specified wait time, and dark mode:

```shell
python3 src/main.py [image-file] -d -t 5 -m
```

Once you're done, you can exit the virtual environment:

On macOS and Linux:

```shell
deactivate
```

On Windows:
```shell
deactivate.bat
```

You can also delete the files associated with it if you want, but you don't have to.
This action cannot be undone.

On macOS and Linux:

```shell
rm -r venv
```

On Windows:
```shell
rmdir /s /q venv
```

## Usage (Visual)

You can also just use a visual editor if you run the program without command line arguments and without specifying a file. You can use arrows, number keys and backspace to move around. Click 'x' to exit and solve the Sudoku.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to modify the instructions based on your project's specific setup and requirements.