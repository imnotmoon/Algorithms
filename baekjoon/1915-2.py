# baekjoon 1915 다시풀기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

ret = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i-1][j-1] == '1':
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
    ret = max(ret, max(dp[i]))

print(ret**2)
