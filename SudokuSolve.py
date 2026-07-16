import copy
sudo = [[0, 6, 0, 0, 0, 0, 4, 1, 5], [0, 0, 5, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0], [7, 0, 3, 6, 0, 0, 0, 0, 0],
        [2, 1, 8, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 1, 0, 0],
        [0, 0, 0, 4, 0, 8, 6, 0, 2], [0, 4, 0, 7, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]]

def check(grid, x, y):
  return rowcheck(grid, y) and colcheck(grid, x) and boxcheck(grid, x, y)

def rowcheck(grid, y):
  seen = set()
  for i in grid[y]:
    if i in seen and i != 0:
      return False
    seen.add(i)
  return True

def colcheck(grid, x):
  seen = set()
  for i in range(len(grid)):
    if grid[i][x] in seen and grid[i][x] != 0:
      return False
    seen.add(grid[i][x])
  return True

def boxcheck(grid, x, y):
  seen = set()
  box = [grid[i][j] for j in range(x//3*3, x//3*3+3) for i in range(y//3*3, y//3*3+3)]
  for k in box:
    if k in seen and k != 0:
      return False
    seen.add(k)
  return True

def disp(grid):
  for row in range(len(grid)):
    for col in range(len(grid)):
      print(grid[row][col] if grid[row][col] != 0 else " ", end=" | " if (col+1) % 3 == 0 else " - ")
    if (row+1)%3 == 0:
      print()
      print("-"*35)
    print()

attempt = copy.deepcopy(sudo)
def empty(grid):
  for i in range(len(grid)):
      for j in range(len(grid)):
        if grid[i][j] == 0:
          return i, j

def solve(grid):
  coords = empty(grid)
  if not coords: return True
  y, x = coords

  for i in range(1, 10):
    grid[y][x] = i
    if check(grid, x, y) and solve(grid):
      return True
    grid[y][x] = 0

  return False

disp(sudo)

for i in range(9):
  ok = True
  for j in range(9):
    if not check(sudo, i, j):
      ok = False
      break
  if not ok:
    print("Invalid")
else:
  print("\nOn solving...")
  solve(attempt)
  disp(attempt)
