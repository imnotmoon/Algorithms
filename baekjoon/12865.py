# baekjoon 12865
n, k = map(int, input().split())
weight, value = [], []
for i in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0 for _ in range(k+1)] for _ in range(n)]

for i in range(n):
    for j in range(1, k+1):
        if j-weight[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
        else:
            dp[i][j] = dp[i-1][j]
    # for j in dp:
    #     print(j)
    # print()

print(dp[n-1][k])
