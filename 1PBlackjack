import random
from google.colab import output
deck = []
shapes = ("♠", "♥", "♦", "♣")

for i in shapes:
  for j in range(2, 11):
    deck.append(str(j)+i)
  for j in "KQJA":
    deck.append(j+i)

random.shuffle(deck)

p1 = []
p2 = []

def draw(p, n):
  for i in range(n):
    if p == 1:
      p1.append(deck.pop(0))
    else:
      p2.append(deck.pop(0))

def disp(dshow):
  output.clear()
  print("Player:", " ".join(p1), "Score:", calc(1))
  if dshow:
    print("Dealer:", " ".join(p2), "Score:", calc(2))
  else:
    print("Dealer:", p2[0], "? "*(len(p2)-1))
  print()

def calc(p):
  sc = 0
  if p == 1:
    for i in p1:
      if i[0] in "KQJ":
        sc+=10
      elif i[0] == "A":
        sc+=11
      else:
        sc+=int(i[:-1])
    a = sum(1 for card in p1 if card.startswith("A"))
    while sc > 21 and a:
      sc-=10
      a-=1
  else:
    for i in p2:
      if i[0] in "KQJ":
        sc+=10
      elif i[0] == "A":
        sc+=11
      else:
        sc+=int(i[:-1])
    a = sum(1 for card in p2 if card.startswith("A"))
    while sc > 21 and a:
      sc-=10
      a-=1
  return sc

draw(1, 2)
draw(2, 2)

disp(False)

g = True

try:
  while True:
    s = input("H - Hit, S - Stand\n").strip().upper()[0]
    if s == "H":
      draw(1, 1)
      if calc(1) > 21:
        print()
        disp(True)
        print("Busted!")
        g = False
        break
    elif s == "S":
      print()
      break
    else:
      print("Invalid input. Try again")
    disp(False)

  while calc(2) < 17 and g:
    draw(2, 1)

  if g:
    disp(True)
    if calc(1) == calc(2):
      print("Draw")
    elif calc(1) > calc(2) or calc(2) > 21:
      print("You win!")
    else:
      print("You lost!")
except IndexError:
  output.clear()
  print("Don't you DARE.")
