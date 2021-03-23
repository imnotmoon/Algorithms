# baekjoon 1309

n = int(input())
dp = [0, 3, 7]
if n < 3:
    print(dp[n])
else:
    for i in range(3, n+1):
        dp.append((dp[i-2]+2*dp[i-1]) % 9901)
    print(dp[n])
