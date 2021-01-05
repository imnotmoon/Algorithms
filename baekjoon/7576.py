import sys
from collections import deque       # list로 만든 큐보다 deque가 훨씬 빠르다

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dq = deque()
m, n = tuple(map(int, input().split()))
box = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if box[i][j] == 1 :
            dq.append((i,j))

while(dq):
    x, y = dq.popleft()
    for i in range(4):
        if (0 <= x+dx[i] < n) and (0 <= y+dy[i] < m) and (box[x+dx[i]][y+dy[i]] == 0) :
            box[x+dx[i]][y+dy[i]] = box[x][y] + 1
            dq.append((x+dx[i], y+dy[i]))

day = 0
for i in range(n) :
    if 0 in box[i] :
        day = 0
        break
    else :
        day = max(day, max(box[i]))

print(day-1)