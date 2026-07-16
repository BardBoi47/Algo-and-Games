import random
weakness = {
  "Electric": ["Ground"],
  "Dark": ["Fairy", "Fighting", "Bug"],
  "Normal": ["Fighting"]
}
resistance = {
  "Electric": ["Flying", "Steel", "Electric"],
  "Dark": ["Ghost", "Dark"],
  "Normal": []
}
nullify = {
  "Dark": ["Psychic"],
  "Electric": [],
  "Normal": ["Ghost"]
}

class Pokemon:
  def __init__(self, name, level, typ1, hp, atk, dEF, moves):
    self.name = name
    self.level = level
    self.typ = typ1
    self.mhp = hp
    self.hp = hp
    self.atk = atk
    self.dEF = dEF
    self.moves = moves
  def attack(self, other, move):
    wrn = 1
    print(self.name, " used ", self.moves[move-1].name, "!", sep="")
    if self.moves[move-1].typ in nullify.get(other.typ):
      print(other.name, "is unaffected!")
      return
    for i in weakness.get(other.typ):
      if self.moves[move-1].typ == i:
        wrn *=2
    for i in resistance.get(other.typ):
      if self.moves[move-1].typ == i:
        wrn /=2
    if wrn > 1:
      print("It's super effective!")
    elif wrn < 1:
      print("It's not effective...")
    if random.randint(1, 100) <= self.moves[move-1].acc:
      dam = (((2*self.level/5 + 2)*self.moves[move-1].power*self.atk/other.dEF)/50+2)*(random.randint(85, 115)/100)*wrn
      if self.typ == self.moves[move-1].typ:
        dam = dam*1.5
      if random.randint(1, 16) == 1:
        dam*=2
        print("A critical hit!")
      dam=int(dam)
      print(other.name,"took",dam,"DMG!")
      other.hp -= dam
      if other.hp <= 0:
        other.hp = 0
        print(other.name, "fainted!")
        print()
      else:
        other.disp(True)
    else:
      print(self.name, "missed!")
  def disp(self, hponly):
    if not hponly:
      print(self.name)
      print("Level:", self.level)
    print("HP: ", "█"*int(self.hp/self.mhp*20), "░"*(20 - int(self.hp/self.mhp*20)), " - ", self.hp, "/", self.mhp, sep = "")
    print()

class Move:
  def __init__(self, name, typ, power, acc):
    self.name = name
    self.typ = typ
    self.power = power
    self.acc = acc

f = Move("Flamethrower", "Fire", 95, 100)
s = Move("Shadow Ball", "Ghost", 80, 100)
e = Move("Ember", "Fire", 40, 100)
fs = Move("False Swipe", "Normal", 40, 100)
ts = Move("Thunder Shock", "Electric", 40, 100)
tb = Move("Thunderbolt", "Electric", 90, 100)
vs = Move("Volt Switch", "Electric", 70, 100)
it = Move("Iron Tail", "Steel", 100, 75)
t = Move("Tackle", "Normal", 40, 100)
po = Move("Pound", "Normal", 40, 100)

z = Pokemon("Zoroark", 50, "Dark", 120, 125, 65, [fs, e, s, f])
p = Pokemon("Pikachu", 45, "Electric", 86, 50, 41, [ts, tb, vs, it])
c = Pokemon("Blissey", 50, "Normal", 315, 10, 140, [po, t, fs, it])

print("A Wild", c.name, "attacked!\n")
z.disp(False)
print()
c.disp(False)
print()

while True:
  for i in range(4):
    print(i+1, "-", z.moves[i].name, "( Power -",z.moves[i].power,"   Accuracy -",z.moves[i].acc,")")
  print("5 - Flee")
  m = int(input())
  if m == 5:
    if random.randint(0, 10) > 1:
      print("Fled successfully.")
      break
    else:
      print("But you were trapped.")
  elif m > 5:
    print("Try again")
    continue

  z.attack(c, m)
  if c.hp <= 0:
    print("You win!")
    break

  c.attack(z, random.randint(1, 4))
  if z.hp <= 0:
    print("You whited out!")
    break

  print()
