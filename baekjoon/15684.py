# baekjoon 15684
import sys
input = sys.stdin.readline
n, m, h = map(int, input().split())
garo = [[0 for _ in range(n+1)] for _ in range(h+1)]
for i in range(m):
    a, b = map(int, input().split())
    garo[a][b] = 1

ladders = []
for i in range(1, h+1):
    for j in range(1, n):
        ladders.append([i, j])
ret = 4


def ladder_down():
    match = 0
    for i in range(1, n+1):  # 각 사다리마다
        dest = i
        for j in range(1, h+1):  # j : 세로 인덱스
            if garo[j][dest] == 1:
                dest = dest + 1
                continue
            if garo[j][dest-1] == 1:
                dest = dest - 1
                continue
        if dest != i:
            return False
    return True


def ladder_place(addition, current_ladder):
    global ret
    if addition > 3:
        return
    if ladder_down():
        ret = min(ret, addition)
        return True
    else:
        for l in range(current_ladder, len(ladders)):
            j, i = ladders[l][0], ladders[l][1]
            if garo[j][i] == 0 and garo[j][i-1] == 0 and garo[j][i+1] == 0:
                garo[j][i] = 1
                ladder_place(addition+1, l)
                garo[j][i] = 0


ladder_place(0, 0)
if ret == 4:
    print(-1)
else:
    print(ret)
