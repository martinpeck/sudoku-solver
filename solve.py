import solver.sudoku_solver
import argparse

def main(puzzle_file_path):

  grid = solver.sudoku_solver.load_grid(puzzle_file_path)
  solver.sudoku_solver.print_grid("Puzzle", grid)
  solved = solver.sudoku_solver.solve_grid(grid)
  solver.sudoku_solver.print_grid("Solution", grid)


parser = argparse.ArgumentParser(description='Sudoku Solver')
parser.add_argument('gridpath', metavar='FILEPATH', help='path to sudoku grid to solve')
args = parser.parse_args()

main(args.gridpath)
