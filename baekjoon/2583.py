# baekjoon 2583
import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
rect = []
for i in range(k):
    rect.append(list(map(int, input().split())))

area = [[0 for _ in range(n)] for _ in range(m)]
for r in rect:
    fx, fy, tx, ty = r[0], r[1], r[2], r[3]
    for i in range(fy, ty):
        for j in range(fx, tx):
            area[i][j] = 2

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(y, x):
    global area
    count = 0
    queue = deque()
    queue.append((y, x))
    area[y][x] = 1
    while queue:
        cy, cx = queue.popleft()
        count += 1
        for i in range(4):
            yy, xx = cy+dy[i], cx+dx[i]
            if (0 <= yy < m) and (0 <= xx < n) and area[yy][xx] == 0:
                area[yy][xx] = 1
                queue.append((yy, xx))
    return count


area_count = 0
area_size = []
for i in range(m):
    for j in range(n):
        if area[i][j] == 0:
            area_size.append(bfs(i, j))
            area_count += 1

print(area_count)
for i in sorted(area_size):
    print(i, end=' ')
