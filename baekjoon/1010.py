# baekjoon 1010
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for j in range(1, n+1):
        dp[j][j] = 1
    for j in range(1, m+1):
        dp[j][1] = j

    for a in range(2, m+1):
        for b in range(2, n+1):
            dp[a][b] = dp[a-1][b-1]+dp[a-1][b]
    print(dp[m][n])
