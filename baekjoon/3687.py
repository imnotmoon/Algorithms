# baekjoon 3687
# dp
import sys

dp = [[sys.maxsize, 0] for i in range(101)]
dp[2], dp[3], dp[4], dp[5], dp[6], dp[7] = [1, 1], [7, 7], [4, 11], [2, 71], [6, 111], [8, 711]

def make_max(n):
    if n < 8:
        return dp[n][1]
    if n%2 == 0:
        return "1"*(n//2)
    else :
        return "7" + ("1"*(n//2 -1))

def make_min(n):
    for j in range(n+1):
        if dp[j][0] < sys.maxsize:
            continue
        for i in range(2, j//2+1):
            if i == 6 :
                dp[j][0] = min(dp[j][0], int("6"+str(dp[j-i][0])), int(str(dp[j-i][0])+"0"), int(str(dp[j-i][0])+"6"))
            elif j-i == 6:
                dp[j][0] = min(dp[j][0], int("6"+str(dp[i][0])), int(str(dp[i][0])+"6"), int(str(dp[i][0])+"0"))
            else :
                dp[j][0] = min(dp[j][0], int(str(dp[i][0])+str(dp[j-i][0])), int(str(dp[j-i][0])+str(dp[i][0])))
    return dp[n][0]


case = int(input())
for i in range(case):
    n = int(input())
    # break n into numbers - min / max
    # min
    if n < 8:
        print(str(dp[n][0]), end=' ')
    else :
        min_val = make_min(n)
        print(min_val, end=' ')
    # max
    max_val = make_max(n)
    print(max_val)
    

