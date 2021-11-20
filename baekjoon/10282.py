# baekjoon 10282

import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start, N):
  dp = [ INF for _ in range(N+1) ]
  dp[start] = 0
  heap = [(0, start)]
  while heap:
    cw, c = heapq.heappop(heap)
    if dp[c] < cw: continue
    for next_node, w in graph[c]:
      if dp[next_node] > cw + w:
        dp[next_node] = cw + w
        heapq.heappush(heap, (cw+w, next_node))
  
  t = 0
  cnt = 0
  for i in dp[1:]:
    if i < INF:
      t = max(i, t)
      cnt += 1

  print(cnt, t)

T = int(input())
for i in range(T):
  N, D, C = map(int, input().split())
  graph = [ [] for _ in range(N+1) ]
  for i in range(D):
    a, b, s = map(int, input().split())
    graph[b].append((a, s))
  dijkstra(C, N)
    

