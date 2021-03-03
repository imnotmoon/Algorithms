# baekjoon 14503
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
r, c, d = map(int, input().split())     # initial point
room = [list(map(int, input().split())) for _ in range(n)]

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
visited = [[0 for _ in range(m)] for _ in range(n)]

count = 0


def clean(r, c):
    global d, room, count
    if visited[r][c] == 0:
        visited[r][c] = 1
        count += 1

    for i in range(4):
        left = (d+3) % 4
        y, x = r+dy[left], c+dx[left]
        if (0 <= y < n) and (0 <= x < m) and visited[y][x] == 0 and room[y][x] == 0:
            d = (d+3) % 4
            clean(y, x)
            return
        else:
            d = (d+3) % 4

        if (i == 3):
            if (0 <= r-dy[d] < n) and (0 <= c-dx[d] < m):
                if room[r-dy[d]][c-dx[d]] == 0:
                    clean(r-dy[d], c-dx[d])
                    return
            else:
                return


clean(r, c)
print(count)
