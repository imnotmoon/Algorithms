# baekjoon 7569

from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
bucket = []
tomato = []
wall = 0
for i in range(h):
    bucket.append([])
    for j in range(n):
        bucket[i].append(list(map(int, input().split())))
        for k in range(len(bucket[i][j])):
            if bucket[i][j][k] == 1:
                tomato.append([i, j, k])
            elif bucket[i][j][k] == -1:
                wall += 1

if len(tomato) == m*n*h - wall:
    print(0)
    exit()

q = deque()
for t in tomato:
    q.append(t)

# 100 010 001 -100 0-10 00-1
dx, dy, dz = [1, 0, 0, -1, 0, 0], [0, 1, 0, 0, -1, 0], [0, 0, 1, 0, 0, -1]
day = 0
fresh = m*n*h-wall-len(tomato)
while q:
    current = q.popleft()
    for i in range(6):
        t = [current[0]+dz[i], current[1]+dy[i], current[2]+dx[i]]
        if (0 <= t[0] < h) and (0 <= t[1] < n) and (0 <= t[2] < m) and bucket[t[0]][t[1]][t[2]] == 0:
            q.append(t)
            bucket[t[0]][t[1]][t[2]] = bucket[current[0]
                                              ][current[1]][current[2]] + 1
            fresh -= 1
            day = bucket[t[0]][t[1]][t[2]]

# for i in range(h):
#     for j in range(n):
#         print(bucket[i][j])
#     print()

print(day-1 if fresh == 0 else -1)
