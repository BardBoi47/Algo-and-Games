def collatz(p, s, n):
  x = n
  stack = {x}
  while True:
    if x % 2 == 0:
      x//=2
    else:
      x = p*x + s
    if x in stack:
      break
    stack.add(x)
  return len(stack)

collatz(3, 1, int(input("Integer: "))) # Let's test some collatz conjecture 3n+1 whatever
