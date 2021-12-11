# baekjoon 2098

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
dist = [ list(map(int, input().split())) for _ in range(N) ]
dp = [ [None] * (1 << N) for _ in range(N) ]
VISITED_ALL = (1 << N) - 1

def tsp(last, visited):
  if visited == VISITED_ALL: return dist[last][0] or INF
  if dp[last][visited] is not None: return dp[last][visited]
  
  tmp = INF
  for city in range(N):
    if visited & (1 << city) == 0 and dist[last][city] != 0:
      tmp = min(tmp, tsp(city, visited | (1 << city)) + dist[last][city])
  dp[last][visited] = tmp
  return tmp

print(tsp(0, 1 << 0))