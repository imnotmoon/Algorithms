# baekjoon 2422

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bad = [ [ 1 for _ in range(N+1) ] for _ in range(N+1) ]
result = 0
for i in range(M):
  a, b = map(int, input().split())
  bad[a][b] = 0
  bad[b][a] = 0

for i in range(1, N+1):
  for j in range(i+1, N+1):
    for k in range(j+1, N+1):
      if bad[i][j] > 0 and bad[i][k] > 0 and bad[k][j] > 0:
        result += 1

print(result)