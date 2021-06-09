# baekjoon 21772 - 가희의 고구마 먹방

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [input() for _ in range(R)]

gahee = [0, 0]
dy, dx = [0,1,0,-1], [1,0,-1,0]

visited = [[False for _ in range(C)] for _ in range(R)]
maxSweetPotato = 0

def backtracking(current_t, y, x, count):
    global new_room
    if current_t == T:
        global maxSweetPotato
        maxSweetPotato = max(maxSweetPotato, count)
        return

    for i in range(4):
        yy, xx = y+dy[i], x+dx[i]
        if (0 <= yy < R) and (0 <= xx < C) and new_room[yy][xx] in ['.', 'S', 'G']:
            # 고구마를 먹을때만 먹음 처리
            if new_room[yy][xx] == 'S':
                new_room[yy][xx] = '.'
                backtracking(current_t+1, yy, xx, count+1)
                new_room[yy][xx] = 'S'
            else :
                backtracking(current_t+1, yy, xx, count)


new_room = []       # ['.......G..'] -> ['.', '.', '.', '.', '.', 'G', '.', '.'] (new_room)
for i in range(R):
    tmp = []
    for j in range(C):
        tmp.append(room[i][j])
        if room[i][j] == 'G': gahee = [i, j]
    new_room.append(tmp)

visited[gahee[0]][gahee[1]] = True
backtracking(0, gahee[0], gahee[1], 0)
print(maxSweetPotato)
