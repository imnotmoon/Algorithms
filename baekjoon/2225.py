# baekjoon 2225

n, k = map(int, input().split())
dp = [[1 for _ in range(n+1)] if i == 0 else [0 for _ in range(n+1)]
      for i in range(k)]

for i in range(1, k):
    for j in range(n+1):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = sum(dp[i-1][:j+1]) % 1000000000

for i in dp:
    print(i)

print(dp[k-1][n] % 1000000000)
