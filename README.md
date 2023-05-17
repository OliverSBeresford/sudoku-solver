# Sudoku Solver
This project is a Sudoku solver that uses a backtracking algorithm to find the solution for a given Sudoku puzzle.

## Prerequisites

- Python 3.6 or above should be installed on your system. If Python is not installed, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your/repository.git

2. Navigate to the project directory:
   ```shell
   cd sudoku-solver
4. Create a virtual environment:
On macOS and Linux:
    ```shell
    python3 -m venv venv
    ```
    On Windows:
    
    ```shell
    py -m venv venv
5. Activate the virtual environment:
On macOS and Linux:
    ```shell
    source venv/bin/activate
    ```
    On Windows:
    ```shell
    venv\Scripts\activate
6. Install the required packages:
    ```shell
    pip install -r requirements.txt
This will install all the necessary dependencies for the project.

# Usage

To solve a Sudoku puzzle, you need to provide the puzzle as input in a specific format. The puzzle should be a text file where each row represents a sudoku in the
sudoku grid. The format would be 0 for empty and a number from 1 to 9 for a filled
square with that number

Example input file (puzzle.txt):

020000000604002030000150040002080070009706800070010300090071000010300607000000080


This means a puzzle like this:

```
0 2 0 0 0 0 0 0 0
6 0 4 0 0 2 0 3 0
0 0 0 1 5 0 0 4 0
0 0 2 0 8 0 0 7 0
0 0 9 7 0 6 8 0 0
0 7 0 0 1 0 3 0 0
0 9 0 0 7 1 0 0 0
0 1 0 3 0 0 6 0 7
0 0 0 0 0 0 0 8 0
```

To solve the puzzle, run the following command:

```shell
python3 solver.py
```
The solution will be displayed in the console.

The puzzles.txt file is given as example input, and it comes with some examples.
If you would like to solve your own puzzles, create a new text file, and 
add your puzzle to it, then put it as a parameter when you run the file.

Once you're done, you can exit the venv:

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to modify the instructions based on your project's specific setup and requirements.