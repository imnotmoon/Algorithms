# baekjoon 2293

n, k = map(int, input().split())
coin = []
dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in range(n):
    coin.append(int(input()))

for c in coin:
    for i in range(1, k+1):
        if i-c >= 0:
            dp[i] = dp[i] + dp[i-c]

print(dp[k])
