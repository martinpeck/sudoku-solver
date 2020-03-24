import solver.sudoku_solver

def main(puzzle_file_path):

  grid = solver.sudoku_solver.load_grid(puzzle_file_path)
  solver.sudoku_solver.print_grid("Puzzle", grid)
  solved = solver.sudoku_solver.solve_grid(grid)
  solver.sudoku_solver.print_grid("Solution", grid)

if __name__ == "__main__":
  main('./puzzles/puzzle-1-grid.txt')
