# baekjoon 16954

import sys
from collections import deque
input = sys.stdin.readline

dy, dx = [1, 0, -1], [1, 0, -1]
board = list(reversed([ list(input().strip()) for _ in range(8) ]))

def bfs():
  queue = deque()
  queue.append((0, 0, 0))
  while queue:
    front = queue.popleft()
    temp = board[front[2]:] + [['.']*8]*front[2]
    if temp[front[0]][front[1]] == '#' : continue
    if front[0] == 7 and front[1] == 7 : return True
    for i in range(3):
      for j in range(3):
        y, x = front[0]+dy[i], front[1]+dx[j]
        if 0 <= y < 8 and 0 <= x < 8:
          if temp[y][x] == '.': queue.append((y, x, front[2]+1))

if bfs(): print(1)
else: print(0)