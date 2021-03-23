# baekjoon 14916
n = int(input())

dp = [1, -1, 1, -1, 2, 1]
if n > 6:
    for i in range(6, n+1):
        minus_2 = dp[i-2]+1 if dp[i-2] > 0 else 0
        minus_5 = 0
        if i > 5:
            minus_5 = dp[i-5]+1 if dp[i-5] > 0 else 0
        if minus_2 > 0 and minus_5 > 0:
            dp.append(min(minus_2, minus_5))
        elif minus_5 == 0:
            dp.append(minus_2)
        elif minus_2 == 0:
            dp.append(minus_5)
        else:
            dp.append(-1)
print(dp[n])
