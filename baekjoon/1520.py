# baekjoon 1520
from sys import stdin
import sys
sys.setrecursionlimit(10**6)
input = stdin.readline

m, n = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(y, x):
    if (y, x) == (m-1, n-1):
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0        # visited
    for i in range(4):
        cy, cx = y+dy[i], x+dx[i]
        if (0<=cy<m) and (0<=cx<n) and arr[cy][cx] < arr[y][x]:
            dp[y][x] += dfs(cy,cx)
    return dp[y][x]

print(dfs(0,0))