import sys
INF = sys.maxsize
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
K = int(input())
graph = [ [] for _ in range(V+1) ]
dp = [ INF for _ in range(V+1) ]
heap = []
for i in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((w, v))

def dijkstra(start):
  dp[start] = 0
  heapq.heappush(heap, (0, start))
  while heap:
    cw, c = heapq.heappop(heap)
    if dp[c] < cw:
      continue
    for w, next_node in graph[c]:
      if dp[next_node] > cw + w:
        dp[next_node] = cw + w
        heapq.heappush(heap, (cw+w, next_node))

dijkstra(K)
for i in range(1, V+1):
  print('INF' if dp[i] == INF else dp[i])
