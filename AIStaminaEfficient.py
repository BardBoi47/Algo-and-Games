# Djikstra you mf

import random
import time
from google.colab import output
import heapq
import sys

L = [[0]+[random.randint(0, 5) for i in range(8)]] + [[random.randint(0, 5) for j in range(9)] for i in range(8)]
st = 100

adj = [[] for i in range(81)]

def tdod(x, y):
  return 9*y+x

def scan():
  for u in range(81):
    y, x = divmod(u, 9)

    # Check neighbors (up, down, left, right)
    # Neighbor 'v' has coordinates (ny, nx)
    # Weight 'w' is L[ny][nx]

    # Up
    if y > 0:
      ny, nx = y - 1, x
      v = tdod(nx, ny)
      w = L[ny][nx]
      adj[u].append((v, w))

    # Down
    if y < 8:
      ny, nx = y + 1, x
      v = tdod(nx, ny)
      w = L[ny][nx]
      adj[u].append((v, w))

    # Left
    if x > 0:
      ny, nx = y, x - 1
      v = tdod(nx, ny)
      w = L[ny][nx]
      adj[u].append((v, w))

    # Right
    if x < 8:
      ny, nx = y, x + 1
      v = tdod(nx, ny)
      w = L[ny][nx]
      adj[u].append((v, w))

def disp():
  output.clear()
  for i in range(9):
    for j in range(9):
      if (i, j) == coords:
        print("🤖", end = " ")
      else:
        print(L[i][j], end = " ")
    print()
  print("\nStamina: ", st)

def dijkstra(src, end):
  V = len(adj)
  pq = []
  dist = [sys.maxsize]*V
  prev = [-1] * V

  dist[src] = 0
  heapq.heappush(pq, (0, src))

  while pq:
    cost, u = heapq.heappop(pq)
    if u == end: break
    if cost > dist[u]: continue

    for v, w in adj[u]:
      if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        prev[v] = u
        heapq.heappush(pq, (dist[v], v))

  return dist, prev

def pathmake(prev, end):
  path = []
  y = end
  while y != -1:
    path.append(y)
    y = prev[y]
  return path[::-1]

scan()
start = tdod(0, 0); end = tdod(8, 8)

dist, prev = dijkstra(start, end)
path = pathmake(prev, end)
path = [divmod(p, 9) for p in path]

coords = divmod(start, 9)

disp()
print("Starting...")
time.sleep(2)

for l in path:
  coords = l
  st-=L[coords[0]][coords[1]]
  disp()
  time.sleep(1.25)
else:
  print("Least stamina:", dist[end])
  print("Path:", path)
