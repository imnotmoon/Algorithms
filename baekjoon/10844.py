# 10844

n = int(input())
dp = [[0 for _ in range(n+1)] for _ in range(10)]
for i in range(10):
    dp[i][1] = 1

for i in range(2, n+1):
    for j in range(10):
        if j-1 >= 0:
            a = dp[j-1][i-1]
        else:
            a = 0
        if j+1 < 10:
            b = dp[j+1][i-1]
        else:
            b = 0
        dp[j][i] = (a+b) % 1000000000

    # for k in dp:
    #     print(k)
    # print()

ret = 0
for i in range(1, 10):
    ret += dp[i][n]
print(ret % 1000000000)
