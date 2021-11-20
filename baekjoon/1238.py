# baekjoon 1238

import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
for i in range(M):
  a, b, t = map(int, input().split())
  graph[a].append((b, t))


fromX = [ INF for _ in range(N+1) ]
shortest_paths = [ INF for _ in range(N+1) ]

def dijkstra(start, dp):
  heap = []
  heapq.heappush(heap, (0, start))
  dp[start] = 0
  while heap:
    cw, c = heapq.heappop(heap)
    if dp[c] < cw: continue
    for next_node, w in graph[c]:
      if dp[next_node] > cw + w:
        dp[next_node] = cw + w
        heapq.heappush(heap, (cw+w, next_node))

for i in range(1, N+1):
  if i != X:
    dp = [ INF for _ in range(N+1) ]
    dijkstra(i, dp)
    shortest_paths[i] = dp[X]
  else : 
    dijkstra(i, fromX)
    shortest_paths[i] = 0

result = 0
for i in range(1, N+1):
  if i == X : continue
  result = max(shortest_paths[i] + fromX[i], result)

print(result)