# baekjoon 1058

import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
graph = [ [0] for _ in range(N+1) ]
for i in range(1, N+1):
  t = input().rstrip()
  for j in range(N):
    if t[j] == 'Y' : 
      graph[i].append(j+1)
      graph[j+1].append(i)

grapht = deepcopy(graph)

for i in range(1, N+1):
  graph[i] = list(set(graph[i]))
  for j in graph[i][1:]:
    for k in graph[j][1:]:
        if k == i : continue
        grapht[i].append(k)
  grapht[i] = list(set(grapht[i]))

result = 0
for i in grapht:
  result = max(result, len(i)-1)

print(result)