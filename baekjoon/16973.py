import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
dy, dx, walls = [1, 0, -1, 0], [0, 1, 0, -1], []
for i in range(N):
  for j in range(M):
    if board[i][j] == 1: walls.append((i, j))
def ca(y, x):
  for Wy, Wx in walls:
    if y <= Wy < y+H and x <= Wx < x+W : return False
  return True
V = [ [0 for _ in range(M)] for _ in range(N) ]
V[Sr-1][Sc-1] = 1
Q = deque([(Sr-1, Sc-1, 0)])
while Q:
  y, x, cnt = Q.popleft()
  if y == Fr-1 and x == Fc-1: 
    print(cnt)
    exit()
  for i in range(4):
    yy, xx = y+dy[i], x+dx[i]
    if 0 <= yy < N and 0 <= xx < M and 0 <= yy+H-1 < N and 0 <= xx+W-1 < M and V[yy][xx] == 0:
      if ca(yy, xx): 
        Q.append((yy, xx, cnt+1))
        V[yy][xx] = 1
print(-1)