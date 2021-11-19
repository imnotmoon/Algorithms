# baekjoon 18352

import sys
input = sys.stdin.readline
INF = sys.maxsize
import heapq

N, M, K, X = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
dp = [ INF for _ in range(N+1) ]
dp[X] = 0
heap = [(0, X)]

while heap:
    cw, c = heapq.heappop(heap)
    if dp[c] < cw: continue
    for next_node, w in graph[c]:
        if dp[next_node] > cw + w:
            dp[next_node] = cw + w
            heapq.heappush(heap, (cw+w, next_node))

result = []
for i in range(len(dp)):
    if dp[i] == K : result.append(i)

if len(result) == 0: print(-1)
else :
    result.sort()
    for i in result:
        print(i)