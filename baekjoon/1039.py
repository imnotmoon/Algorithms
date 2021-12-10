# baekjoon 1039

from itertools import combinations
from collections import deque

N, K = map(int, input().split())
N, result = str(N), -1
comb = list(combinations(range(len(N)), 2))
q = deque([N])

def bfs():
  c = set()
  qlen = len(q)
  ans = -1
  while qlen:
    s = q.popleft()
    for j, i in comb:
      t = list(s); t[i], t[j] = t[j], t[i]; t = ''.join(t)
      if t[0] == '0': continue
      if t not in c:
        ans = max(ans, int(t))
        c.add(t); q.append(t)
    qlen -= 1
  return ans
  
for _ in range(K, 0, -1): result = bfs()
print(result)