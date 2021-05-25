# baekjoon 11048
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = maze[0][0]

for i in range(n):
    for j in range(m):
        if 0 <= i-1 and 0 <= j-1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+maze[i][j])
        if 0 <= i-1 :
            dp[i][j] = max(dp[i][j], dp[i-1][j]+maze[i][j])
        if 0 <= j-1 :
            dp[i][j] = max(dp[i][j], dp[i][j-1]+maze[i][j])

print(dp[n-1][m-1])
