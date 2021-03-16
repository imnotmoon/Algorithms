# beakjoon 12865 다시풀기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
weight, value = [], []
for i in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= weight[i-1]:
            dp[i][j] = max(dp[i-1][j], value[i-1] + dp[i-1][j-weight[i-1]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
