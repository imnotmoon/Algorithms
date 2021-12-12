import sys
import heapq
input = sys.stdin.readline

N = int(input())
classes = sorted([ list(map(int, input().split())) for _ in range(N) ], key=lambda x: x[0])
end = [classes[0][1]]
for time in classes[1:]:
  if end[0] <= time[0]: heapq.heappop(end)
  heapq.heappush(end, time[1])

print(len(end))