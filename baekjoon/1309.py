# baekjoon 1309

n = int(input())
dp = [0, 3, 7]
if n == 1:
    print(3)
elif n == 2:
    print(7)
else:
    for i in range(3, n+1):
        dp.append((dp[i-2]+2*dp[i-1]) % 9901)
    print(dp[n])
