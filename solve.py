import solver.sudoku_solver

def main():

  grid = solver.sudoku_solver.load_puzzle('./puzzles/puzzle-3.txt')
  solver.sudoku_solver.print_grid("Puzzle", grid)
  solved = solver.sudoku_solver.solve_grid(grid)
  solver.sudoku_solver.print_grid("Solution", grid)

if __name__ == "__main__":
  main()
