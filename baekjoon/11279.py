import heapq
import sys
input = sys.stdin.readline
heap = []

n = int(input())
for _ in range(n):
  i = int(input())
  if i == 0:
    if len(heap) == 0 : print(0)
    else : 
      print(heapq.heappop(heap)[1])
  else :
    heapq.heappush(heap, (-i, i))