# baekjoon 19236 다시풀기

import sys
from collections import deque
import copy
input = sys.stdin.readline

dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
answer = 0

# board[0] : 물고기 번호, board[1] : 물고기 방향
board = [[[[] for _ in range(4)] for _ in range(4)] for _ in range(2)]

for i in range(4):
    t = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0 : board[0][i][j//2] = t[j]
        else : board[1][i][j//2] = t[j]

def search_fish(idx, b):
    for i in range(4):
        for j in range(4):
            if b[0][i][j] == idx : return (i, j, b[1][i][j])
    return (-1, -1, -1)

def move_fish(b, shark_y, shark_x):
    for i in range(1, 17):
        y, x, d = search_fish(i, b)
        if y < 0 : continue  # 이미 먹힌 물고기
        for j in range(d, d+8):
            yy, xx = y + dy[j%9 if j < 9 else j%8], x + dx[j%9 if j < 9 else j%8]
            if 0 <= yy < 4 and 0 <= xx < 4:
                if(shark_y == yy and shark_x == xx) : continue
                b[0][y][x], b[0][yy][xx] = b[0][yy][xx], b[0][y][x]
                b[1][y][x], b[1][yy][xx] = b[1][yy][xx], b[1][y][x]
                b[1][yy][xx] = j%9 if j < 9 else j%8
                break
    return b

        
def dfs(arr, shark_y, shark_x, total):
    global answer
    b = copy.deepcopy(arr)
    total += b[0][shark_y][shark_x]
    answer = max(answer, total)
    b[0][shark_y][shark_x] = -1

    b = move_fish(b, shark_y, shark_x)
    y, x = shark_y, shark_x
    for _ in range(4):
        y, x = y+dy[b[1][shark_y][shark_x]], x+dx[b[1][shark_y][shark_x]]
        if 0 <= y < 4 and 0 <= x < 4 and b[0][y][x] > 0:
            dfs(b, y, x, total)

dfs(board, 0, 0, 0)
print(answer)