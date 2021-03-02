# baekjoon 2630

import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white_blue = [0, 0]


def divide_paper(from_x, from_y, to_x, to_y):
    # print(from_x, from_y, to_x, to_y)
    # 종료조건 1 : 크기가 1인 경우
    if to_x-from_x == 1:
        if paper[from_y][from_x] == 1:
            white_blue[1] += 1
            return 1
        else:
            white_blue[0] += 1
            return 0
    # 종료조건 2 : 모든 칸이 0 또는 1인 경우
    cnt = 0
    for i in range(from_y, to_y):
        for j in range(from_x, to_x):
            cnt += paper[i][j]
    if cnt == 0:
        white_blue[0] += 1
        return 0
    elif cnt == (to_x-from_x) * (to_y-from_y):
        white_blue[1] += 1
        return 1

    # 분할
    mid = (to_x-from_x)//2
    return divide_paper(from_x, from_y, from_x+mid, from_y+mid) + \
        divide_paper(from_x+mid, from_y+mid, to_x, to_y) + \
        divide_paper(from_x, from_y+mid, from_x+mid, to_y) + \
        divide_paper(from_x+mid, from_y, to_x, from_y+mid)


divide_paper(0, 0, n, n)
print(white_blue[0])
print(white_blue[1])
