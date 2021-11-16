# baekjoon 1043
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
knowns = (list(map(int, input().split())))[1:]
parties = [ list(map(int, input().split())) for _ in range(M) ]

visited = [ 0 for _ in range(N+1) ]
for i in knowns:
  visited[i] = 1
result = [ 1 for _ in range(M+1) ]
q = deque(knowns)
while q:
  person = q.popleft()
  for i in range(M):
    if result[i] == 1 and person in parties[i][1:]:
      result[i] = 0
      for j in parties[i][1:]:
        if visited[j] == 0 :
          q.append(j)
          visited[j] = 1

print(sum(result)-1)