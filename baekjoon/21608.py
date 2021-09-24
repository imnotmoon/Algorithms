# baekjoon 21608
import sys
input = sys.stdin.readline

n = int(input())
likes = dict()
seats = [[0 for _ in range(n)] for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n**2):
    t = list(map(int, input().split()))
    likes[t[0]] = t[1:]

def seat(arr):
    candidates = []
    for i in range(n):
        for j in range(n):
            if seats[i][j] != 0: continue
            empty, friends = 0, 0
            for k in range(4):
                y, x = i+dy[k], j+dx[k]
                if 0 <= y < n and 0 <= x < n:
                    if seats[y][x] == 0 : empty += 1
                    if seats[y][x] in arr: friends += 1
            candidates.append([i, j, friends, empty])

    candidates = sorted(candidates, key=lambda x : (x[2], x[3], -x[0], -x[1]))
    to_y, to_x = candidates[-1][0], candidates[-1][1]
    return to_y, to_x

# fill seats
for key in likes.keys():
    y, x = seat(likes[key])
    seats[y][x] = key

satisifaction = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            y, x = i+dy[k], j+dx[k]
            if 0 <= y < n and 0 <= x < n:
                if seats[y][x] in likes[seats[i][j]]: cnt += 1
        satisifaction += 0 if cnt == 0 else 10**(cnt-1)

print(satisifaction)