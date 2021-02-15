# baekjoon 14502

import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

# 1. 벽 치기 : 1, 2가 아닌 곳에
# 2. bfs -> 안전영역 세기


def bfs(lab):
    q = deque()
    for v in virus:
        q.append(v)

    # bfs
    while q:
        current = q.popleft()
        for i in range(4):
            cy, cx = current[0]+dy[i], current[1]+dx[i]
            if(0 <= cy < N) and (0 <= cx < M) and lab[cy][cx] == 0:
                lab[cy][cx] = 2
                q.append((cy, cx))

    safe = 0
    for i in lab:
        safe += i.count(0)

    return safe


virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))

safe = 0
for i in range(N*M):
    if arr[i//M][i % M] == 0:
        w1 = (i//M, i % M)
        for j in range(i+1, N*M):
            if arr[j//M][j % M] == 0:
                w2 = (j//M, j % M)
                for k in range(j+1, N*M):
                    if arr[k//M][k % M] == 0:
                        w3 = (k//M, k % M)

                        wall_arr = copy.deepcopy(arr)

                        wall_arr[w1[0]][w1[1]], wall_arr[w2[0]][w2[1]
                                                                ], wall_arr[w3[0]][w3[1]] = 1, 1, 1
                        # for a in wall_arr:
                        #     print(a)
                        safe = max(safe, bfs(wall_arr))

print(safe)
