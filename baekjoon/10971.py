# baekjoon 10971

import sys
input = sys.stdin.readline

N = int(input())
links = [ list(map(int, input().split())) for _ in range(N) ]
VISITED_ALL = (1 << N) - 1
ans = sys.maxsize

def bt(start, last, visited, cost):
  global ans
  if visited == VISITED_ALL:
    if links[last][start] > 0:
      ans = min(ans, cost + links[last][start])
      return
  for city in range(N):
    if links[last][city] > 0 and visited & (1 << city) == 0:
      bt(start, city, visited | (1 << city), cost + links[last][city])

bt(1, 1, 1 << 1, 0)
print(ans)
