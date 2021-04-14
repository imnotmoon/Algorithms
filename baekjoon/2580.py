# baekjoon 2580 스도쿠
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]


def square(y, x, val):
    nx = x//3 * 3
    ny = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == board[ny+i][nx+j]:
                return False
    return True


def fill(zero_idx):
    if zero_idx == len(zeros):
        for ii in board:
            for jj in ii:
                print(jj, end=' ')
            print()
        sys.exit(0)

    y, x = zeros[zero_idx][0], zeros[zero_idx][1]
    for i in range(1, 10):
        column, row = board[y][:], [k[x] for k in board]
        if i not in column and i not in row:
            # 3x3

            # 이건 왜 안될까
            # for yy in range(y//3*3, y//3*3+3):
            #     for xx in range(x//3*3, x//3*3+3):
            #         if i != board[yy][xx]:
            #

            if square(y, x, i):
                board[y][x] = i
                fill(zero_idx+1)
                board[y][x] = 0


fill(0)
