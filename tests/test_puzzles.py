import solver.sudoku_solver as solver
import pytest

@pytest.mark.parametrize("grid_file_path, solution_file_path", [("./puzzles/puzzle-1-grid.txt","./puzzles/puzzle-1-solution.txt"),
                                                                ("./puzzles/puzzle-2-grid.txt","./puzzles/puzzle-2-solution.txt"),
                                                                ("./puzzles/puzzle-3-grid.txt","./puzzles/puzzle-3-solution.txt")])
def test_puzzle(grid_file_path, solution_file_path):
  puzzle_grid = solver.load_puzzle(grid_file_path)
  expected_grid = solver.load_puzzle(solution_file_path)

  result = solver.solve_grid(puzzle_grid)

  assert puzzle_grid == expected_grid

