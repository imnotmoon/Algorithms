# baekjoon 12851
from collections import deque

n, m = map(int, input().split())
min_time = 100000
cnt = [0] * 100001

def bfs():
  global min_time, cnt
  q = deque([(n, 0)])
  visited = [False] * 100001
  while q:
    x, t = q.popleft()
    if x == m:
      cnt[t] += 1
      min_time = min(min_time, t)
      continue
    else :
      visited[x] = True
    if 2*x <= 100000 and not visited[2*x] : q.append((2*x, t+1))
    if x-1 >= 0 and not visited[x-1] : q.append((x-1, t+1))
    if x+1 <= 100000 and not visited[x+1] : q.append((x+1, t+1))

bfs()
print(min_time)
print(cnt[min_time])