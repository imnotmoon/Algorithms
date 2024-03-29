# baekjoon 13975

import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
  input()
  heap, result = [], 0
  for i in list(map(int, input().split())): heapq.heappush(heap, i)
  while len(heap) > 1:
    t = heapq.heappop(heap) +heapq.heappop(heap)
    result += t
    heapq.heappush(heap, t)
  print(result)
