# baekjoon 1987
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [input() for _ in range(r)]

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

q = set([(0, 0, board[0][0])])
ret = 1
while q:
    y, x, ans = q.pop()
    for i in range(4):
        cy, cx = y+dy[i], x+dx[i]
        if (0 <= cy < r) and (0 <= cx < c) and board[cy][cx] not in ans:
            q.add((cy, cx, ans + board[cy][cx]))
            ret = max(ret, len(ans+board[cy][cx]))
print(ret)
