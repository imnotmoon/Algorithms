# baekjoon 2109

import sys, heapq
input = sys.stdin.readline

n = int(input())
requests = sorted([ list(map(int, input().split())) for _ in range(n) ], key=lambda x:(x[1]))

heap, total = [], 0
for req in requests:
  if len(heap) >= req[1]:
    if heap[0] < req[0]:
      heapq.heappop(heap)
      heapq.heappush(heap, req[0])
  else :
    heapq.heappush(heap, req[0])

for i in heap:
  total += i
print(sum(heap))