import random as r
from google.colab import output

world = []
pos = [4, 5]
enemy = [r.randint(0, 9), r.randint(0, 9)]
end = [r.randint(0, 9), r.randint(0, 9)]

while end == pos:
  end = [r.randint(0, 9), r.randint(0, 9)]
while enemy == end or enemy == pos:
  enemy = [r.randint(0, 9), r.randint(0, 9)]

gs = True
for i in range(10):
  world.append([])
  for j in range(10):
    if [i, j] == enemy:
      world[i].append("👹")
    elif [i, j] == pos:
      world[i].append("👤")
    elif [i, j] == end:
      world[i].append("🏁")
    else:
      world[i].append("🌳")

def disp():
  output.clear()
  for i in range(10):
    for j in range(10):
      print(world[i][j], end = " ")
    print()
def update():
  for i in range(10):
    for j in range(10):
      if [i, j] == enemy:
        world[i][j] = "👹"
      elif [i, j] == pos:
        world[i][j] = "👤"
      elif [i, j] == end:
        world[i][j] = "🏁"
      else:
        world[i][j] = "🌳"
"""
def enmove(m):
  y = enemy[0]; x = enemy[1]
  if m == 0 and y-1 != end[0] and y > 0:
    enemy[0] -= 1
  elif m == 1 and x-1 != end[1] and x > 0:
    enemy[1] -= 1
  elif m == 2 and y+1 != end[0] and y < 9:
    enemy[0] += 1
  elif m == 3 and x+1 != end[1] and x < 9:
    enemy[1] += 1
"""

def smartenmove():
  y = abs(pos[0] - enemy[0]); x = abs(pos[1] - enemy[1])
  if max(x, y) == y:
    if pos[0] > enemy[0]:
      enemy[0] += 1
    elif pos[0] < enemy[0]:
      enemy[0] -= 1
  else:
    if pos[1] > enemy[1]:
      enemy[1] += 1
    elif pos [1] < enemy[1]:
      enemy[1] -= 1

disp()
print("W - Up\nA - Left\nS - Down\nD - Right\nOther - Quit")
for i in range(20):
  print("\n", 20-i, " moves remain", sep="")
  press = input().strip().upper()[0]
  if press == "W":
    if pos[0] > 0:
      pos[0] -= 1
  elif press == "A":
    if pos[1] > 0:
      pos[1] -= 1
  elif press == "S":
    if pos[0] < len(world)-1:
      pos[0] += 1
  elif press == "D":
    if pos[1] < len(world[0])-1:
      pos[1] += 1
  else:
    print("Terminating...")
    break
  smartenmove()
  update()
  disp()
  if pos == enemy:
    print("Game over!")
    break
  if pos == end:
    print("You win!")
    break
else:
  print("You lost!")
