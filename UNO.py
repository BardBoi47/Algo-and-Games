import random as r
from google.colab import output
import time

deck = []
discard = []

for i in range(10):
  for j in "🟥🟦🟩🟨":
    if i == 0:
      deck.append((str(i), j))
    else:
      deck.extend([(str(i), j) for k in range(2)])

deck.extend([["Wild", ""] for i in range(4)])
deck.extend([["Wild +4", ""] for i in range(4)])
for i in "🟥🟦🟩🟨":
  deck.extend([("+2", i)]*2)
  deck.extend([("Reverse", i)]*2)
  deck.extend([("Skip", i)]*2)

r.shuffle(deck)

pl = []

def draw(p, n):
  global deck, discard;
  for i in range(n):
    pl[p].append(deck.pop(0))
    if len(deck) == 0:
      print("Deck ran out, taking from discard pile...")
      deck = discard[:-1]
      random.shuffle(deck)
      discard = [discard[-1]]

n = -1
while n <= 0 or n >= 7:
  n = int(input("No. of players: "))
  if n <= 0 or n >= 7:
    print("Invalid. Try again.")

for i in range(n):
  pl.append([])
  draw(i, 7)

def disp(p):
  output.clear()
  print("Recentmost Discarded Card:", *discard[-1])
  print(f"Player {p+1}'s hand:", end = " ")
  for i, card in enumerate(pl[p]):
    print(f"{i}. {' '.join(card)}", end = " ")
  print()

discard.append(deck.pop(0))
disp(0)

color = "🟥🟦🟩🟨"
wi = -1; turn, step, wild = 0, 1, color[r.randint(0, 3)]
while wi < 0:
  disp(turn)
  if not (any(i[0] == discard[-1][0] or i[1] == discard[-1][1] or "Wild" in i[0] for i in pl[turn])):
    print("You don't have a throwable card. You draw a card.")
    draw(turn, 1)
    turn+=step
    turn=turn%len(pl)
    time.sleep(3)
    continue
  throw = int(input())
  if pl[turn][throw][0] == discard[-1][0] or pl[turn][throw][1] == discard[-1][1]:
    if pl[turn][throw][0] == "Reverse":
      output.clear()
      print(f"Player {turn+1} reversed the turn order!")
      step*=-1
      time.sleep(3)
    elif pl[turn][throw][0] == "Skip":
      output.clear()
      print(f"Player {turn+1} skipped the next player's turn")
      step*=2
      time.sleep(3)
    elif pl[turn][throw][0] == "+2":
      output.clear()
      print(f"Player {(turn+step)%len(pl)+1} draws 2 cards!")
      draw((turn+step)%len(pl), 2)
      step*=2
      time.sleep(3)
    discard.append(pl[turn].pop(throw))
    if len(pl[turn]) == 1:
      print(f"Player {turn+1} yells Uno!")
      time.sleep(3)
    elif len(pl[turn]) == 0:
      wi = turn+1
      break
    turn+=step
  elif "Wild" in pl[turn][throw][0]:
    print("🟥 - 1, 🟦 - 2, 🟩 - 3, 🟨 - 4")
    while True:
      wc = int(input())-1
      if wc in range(0, 4):
        break
      print("Invalid, try again~")
    pl[turn][throw][1] = color[wc]
    output.clear()
    print(f"Player {turn+1} changed the colour to {color[wc]}")
    discard.append(pl[turn].pop(throw))
    if len(pl[turn]) == 1:
      print(f"Player {turn+1} yells Uno!")
      time.sleep(3)
    elif len(pl[turn]) == 0:
      wi = turn%len(pl)+1
      break
    if "+4" in discard[-1][0]:
      print(f"Player {(turn+step)%len(pl)+1} draws 4 cards!")
      draw((turn+step)%len(pl), 4)
      step*=2
    turn+=step
    time.sleep(4)
  else:
    print("No, silly! Throw another card.")
    time.sleep(3)
  turn=turn%len(pl)
  step//=abs(step)

print(f"Player {wi} wins!")
