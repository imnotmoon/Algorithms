# baekjoon 1753

import sys
input = sys.stdin.readline
INF = sys.maxsize
import heapq

V, E = map(int, input().split())
K = int(input())

graph = [ [] for _ in range(V+1) ]
dp = [INF for _ in range(V+1)] # 최단경로 저장
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
      # dp[c](현재 노드까지 오는 최단경로)보다 비싼 값을 치르고 온 경우
      # visited가 없어서 이렇게 처리
      continue
    for w, next_node in graph[c]:
      if w + cw < dp[next_node]:
        dp[next_node] = w + cw
        heapq.heappush(heap, (w+cw, next_node))

dijkstra(K)
for i in range(1, V+1):
  print("INF" if dp[i] == INF else dp[i])
