def load_grid(file):
  grid = []
  with open(file, 'r') as f:
    for line in f.readlines():
      grid_line = [int(cell) for cell in line.strip()]
      grid.append(grid_line)
  return grid

def print_grid(description, grid):
  print(f"{description}: ")

  for counter, row in enumerate(grid):
    if counter % 3 == 0:
      print("")

    row_text = f"{grid[counter][0]}{grid[counter][1]}{grid[counter][2]} {grid[counter][3]}{grid[counter][4]}{grid[counter][5]} {grid[counter][6]}{grid[counter][7]}{grid[counter][8]}"
    print(row_text)

  print("")

def is_valid_solution(grid, row, col, solution):

  # check the row
  for item in grid[row]:
    if item == solution:
      return False

  # check the column
  for row_counter in range(0,9):
    if grid[row_counter][col] == solution:
      return False

  # check the squares
  grid_x = col // 3
  grid_y = row // 3

  rows_start = grid_y * 3
  rows_end = rows_start + 3

  cols_start = grid_x * 3
  cols_end = cols_start + 3

  for grid_row in range(rows_start, rows_end):
    for grid_col in range(cols_start, cols_end):
      if grid[grid_row][grid_col] == solution:
        return False

  return True

def solve_grid(grid):

  for row in range(0, 9):
    for col in range(0, 9):
      if grid[row][col] == 0:
        for solution in range (1, 10):
          if is_valid_solution(grid, row, col, solution):
            grid[row][col] = solution
            solved = solve_grid(grid)
            if solved:
              return True
            else:
              grid[row][col] = 0
        return False

  return True
