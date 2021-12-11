# baekjoon 10971

import sys
input = sys.stdin.readline

N = int(input())
links = [ list(map(int, input().split())) for _ in range(N) ]
ans = sys.maxsize
cost = 0

def bt(visited):
  global ans, cost
  if len(visited) == N:
    if links[visited[-1]][0] > 0:
      ans = min(ans, cost + links[visited[-1]][0])
      return
  for i in range(N):
    if links[visited[-1]][i] > 0 and i not in visited:
      cost += links[visited[-1]][i]
      bt(visited + [i])
      cost -= links[visited[-1]][i]

bt([0])
print(ans)
