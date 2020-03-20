
def print_grid(description, grid):
  print(f"{description}: ")

  for row in grid:
    row_text = " ".join(row)
    print(row_text)

  print("")

def solve_puzzle(grid):
  return grid


def solve():

  grid = load_puzzle('puzzle.txt')
  print_grid("Puzzle", grid)

  solution_grid = solve_puzzle(grid)
  print_grid("Solution", solution_grid)

def load_puzzle(file):
  grid = []
  with open(file, 'r') as f:
    for line in f.readlines():
      grid_line = list(line.strip())
      grid.append(grid_line)
  return grid

if __name__ == "__main__":
  solve()