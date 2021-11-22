# baekjoon 11404
import sys
input = sys.stdin.readline
INF = 10000001
N, M = int(input()), int(input())
bus = [ [INF for _ in range(N+1) ] for _ in range(N+1) ]
for i in range(1, N+1):
  bus[i][i] = 0
for i in range(M):
  a, b, c = map(int, input().split())
  bus[a][b] = min(bus[a][b], c)

for i in range(1, N+1):  # i번 노드를 거쳐감
  for s in range(1, N+1):
    for e in range(1, N+1):
      if s == e : continue
      bus[s][e] = min(bus[s][e], bus[s][i] + bus[i][e])

for i in range(N+1):
  for j in range(N+1):
    if bus[i][j] == INF:
      bus[i][j] = 0

for i in bus[1:]:
  for j in i[1:]:
    print(j, end=' ')
  print()
