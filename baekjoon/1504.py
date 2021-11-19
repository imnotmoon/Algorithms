# baekjoon 1504

import sys
INF = sys.maxsize
input = sys.stdin.readline
import heapq

N, E = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
for i in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
v1, v2 = map(int, input().split())

dp1 = [ INF for _ in range(N+1) ]  # from start
dp2 = [ INF for _ in range(N+1) ]  # from v1 
dp3 = [ INF for _ in range(N+1) ]  # from v2

def dijkstra(start, dp):
  heap = []
  heapq.heappush(heap, (0, start))
  dp[start] = 0
  t = []
  while heap:
    cw, c = heapq.heappop(heap)
    if dp[c] < cw : continue
    for next_node, w in graph[c]:
      if next_node == c : continue
      if dp[next_node] > cw + w :
        dp[next_node] = cw + w
        heapq.heappush(heap, (cw+w, next_node))

dijkstra(1, dp1)
dijkstra(v1, dp2)
dijkstra(v2, dp3)

if INF in [dp1[v1], dp2[v2], dp3[N]] :
  if INF in [dp1[v2], dp3[v1], dp2[N]]:
    print(-1)
    exit(0)


route1 = dp1[v1] + dp2[v2] + dp3[N]
route2 = dp1[v2] + dp3[v1] + dp2[N]

if route1 < route2 : 
  print(route1)
else :
  print(route2)