# baekjoon 1916

import sys
input = sys.stdin.readline
INF = sys.maxsize
import heapq

N = int(input())
M = int(input())
bus = [ [] for _ in range(N+1) ]
for i in range(M):
  u, v, w = map(int, input().split())
  bus[u].append((v, w))
A, B = map(int, input().split())

heap = []
dp = [ INF for _ in range(N+1) ]

def dijkstra():
  dp[A] = 0
  heapq.heappush(heap, (0, A))
  
  while heap:
    wc, c = heapq.heappop(heap)
    if dp[c] < wc : continue
    for next_node, w in bus[c]:
      if dp[next_node] > wc + w: 
        dp[next_node] = wc + w
        heapq.heappush(heap, (wc+w, next_node))

dijkstra()
print(dp[B])


