# baekjoon 2583
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
rect = []
for i in range(k):
    rect.append(list(map(int, input().split())))

area = [[0 for _ in range(n)] for _ in range(m)]
for r in rect:
    fy, fx, ty, tx = r[0], r[1], r[2], r[3]
    for i in range(fy, fy+ty):
        for j in range(fx, fx+tx):
            area[i][j] = 1

for i in area:
    print(area)
