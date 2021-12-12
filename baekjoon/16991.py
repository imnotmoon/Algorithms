# baekjoon 16991

import sys
import math
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
cor = [ list(map(int, input().split())) for _ in range(N) ]
VISITED_ALL = (1 << N) - 1
dp = [ [None]*(1 << N) for _ in range(N) ]
dist = [ [0 for _ in range(N)] for _ in range(N) ]

for i in range(N):
  for j in range(N):
    if i == j : continue
    dist[i][j] = math.sqrt((cor[i][0] - cor[j][0])**2 + (cor[i][1] - cor[j][1])**2)

def tsp(last, visited):
  if visited == VISITED_ALL: return dist[last][0] or INF
  if dp[last][visited] is not None: return dp[last][visited]

  tmp = INF
  for city in range(N):
    if visited & (1 << city) == 0 and dist[last][city] > 0:
      tmp = min(tmp, tsp(city, visited | (1 << city)) + dist[last][city])
  dp[last][visited] = tmp
  return tmp

print(tsp(0, 1 << 0))