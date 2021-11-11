# beakjoon 16973
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
walls = []

for i in range(N):
  for j in range(M):
    if board[i][j] == 1: walls.append((i, j))

def check_available(y, x):
  for Wy, Wx in walls:
    if y <= Wy < y+H and x <= Wx < x+W : 
      return False
  return True

visited = [ [0 for _ in range(M)] for _ in range(N) ]
visited[Sr-1][Sc-1] = 1
queue = deque([(Sr-1, Sc-1, 0)])
while queue:
  y, x, cnt = queue.popleft()
  if y == Fr-1 and x == Fc-1: 
    print(cnt)
    exit()
  for i in range(4):
    yy, xx = y+dy[i], x+dx[i]
    if 0 <= yy < N and 0 <= xx < M and 0 <= yy+H-1 < N and 0 <= xx+W-1 < M and visited[yy][xx] == 0:
      if check_available(yy, xx): 
        queue.append((yy, xx, cnt+1))
        visited[yy][xx] = 1
print(-1)