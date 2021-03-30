# baejoon 1715

import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

cnt = 0
while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    cnt += (a+b)

print(cnt)
