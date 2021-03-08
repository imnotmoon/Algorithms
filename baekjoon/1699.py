# baekjoon 1699

n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i] = i
    # j = 1
    # while((j*j) <= i):
    #     dp[i] = min(dp[i], dp[i-(j*j)]+1)
    #     j += 1
    for j in range(1, i):
        if (j*j) > i:
            break
        dp[i] = min(dp[i], dp[i-(j*j)]+1)

print(dp[n])
