# baekjoon 2665

# 일단 벽을 안부시고 이동하는게 최우선이지만
# 벽을 부셔야 할 경우까지 계산

import sys
import heapq
input = sys.stdin.readline

N = int(input())
room = [ list(map(int, input().rstrip())) for _ in range(N) ]
visit = [ [0 for _ in range(N)] for _ in range(N) ]

def dijkstra():
  dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
  heap = []
  heapq.heappush(heap, [0, 0, 0])
  visit[0][0] = 1
  while heap:
    a, y, x = heapq.heappop(heap)
    if x == N-1 and y == N-1:
      print(a)
      return
    for i in range(4):
      yy, xx = y+dy[i], x+dx[i]
      if 0 <= yy < N and 0 <= xx < N and visit[yy][xx] == 0:
        visit[yy][xx] = 1
        if room[yy][xx] == 0:
          heapq.heappush(heap, [a+1, yy, xx])
        else:
          heapq.heappush(heap, [a, yy, xx])

dijkstra()

