# baekjoon 21278

import sys
input = sys.stdin.readline
from itertools import combinations
import heapq
INF = sys.maxsize

N, M = map(int, input().split())
roads = [ [0 if i == j else INF for j in range(N+1)] for i in range(N+1) ]
results = []
for i in range(M):
  a, b = map(int, input().split())
  roads[a][b], roads[b][a] = 1, 1

def fw():
  for i in range(1, N+1):
    for s in range(1, N+1):
      for e in range(1, N+1):
        if s == e : continue
        roads[s][e] = min(roads[s][i]+roads[i][e], roads[s][e])

def s(f1, f2):
  r = 0
  for i in range(1, N+1):
    if roads[f1][i] == INF or roads[f2][i] == INF: return INF
    r += min(roads[f1][i], roads[f2][i])
  return r

fw()

for c in combinations(range(1, N+1), 2):
  r = s(c[0], c[1])
  if r == INF: continue
  t = [min(c[0], c[1]), max(c[0], c[1]), r*2]
  heapq.heappush(results, ((t[2], t[0], t[1]), t))

print(*results[0][1])


