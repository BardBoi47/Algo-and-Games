import random
from google.colab import output

stack = []
coords = (0, 0)
apple = ()
score = 0

def layout():
  output.clear()
  print("WASD to move\n")
  for i in range(9):
    for j in range(9):
      if (i, j) == coords:
        print("🟢", end = " ")
      elif (i, j) in stack:
        if (i, j) == stack[0]:
          print("🥬", end = " ")
        else: print("🟩", end = " ")
      elif (i, j) == apple:
        print("🍎", end = " ")
      else:
        print("🟦", end = " ")
    print()
  print()

def update():
  while len(stack) > score:
    stack.pop(0)

def genapple():
  global apple
  apple = (random.randint(0, 8), random.randint(0, 8))
  if apple == coords or apple in stack:
    genapple()

genapple()

try:
  while score < 80:
    layout()
    s = input().strip().upper()[0]
    stack.append(coords)
    if s == "W":
      coords = ((coords[0]-1)%9, coords[1])
    elif s == "D":
      coords = (coords[0], (coords[1]+1)%9)
    elif s == "A":
      coords = (coords[0], (coords[1]-1)%9)
    elif s == "S":
      coords = ((coords[0]+1)%9, coords[1])
    else:
      print("Stop it. Get some help.")
    update()
    if coords in stack:
      output.clear()
      print("Crash! You lost.")
      print("Score:", score)
      break
    elif coords == apple:
      score += 1
      genapple()
  else:
    output.clear()
    print("You won!")
    print("Score:", score)
except IndexError:
  output.clear()
  print("Don't even try it.")
