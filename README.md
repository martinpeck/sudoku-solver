# Sudoku Solver

This is a simple Python script that solves Sudoku puzzles. It solves the puzzle by essentially "brute force".

## Running this Code

## How it Works

Each empty cell is visited, starting top left, left to right, row by row, until the very last cell (bottom right) is reached. For empty cells, the numbers from 1 to 9 are, in turn, are tried in that cell. If the puzzle allows a given number to be attempted then the grid is updated, and the next empty cell is visited.

 
