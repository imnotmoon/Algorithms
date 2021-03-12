# baekjoon 11057
n = int(input())
dp = [[10-i for i in range(10)] if j == 0 else [0 for _ in range(10)]
      for j in range(n)]
for i in range(1, n):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:]) % 10007
if n == 1:
    print(10)
else:
    print(dp[n-1][0] % 10007)
