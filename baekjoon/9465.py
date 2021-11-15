# baekjoon 9465
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n = int(input())
    numbers = [ list(map(int, input().split())) for _ in range(2) ]
    dp = [ [0 for _ in range(n)] for _ in range(2) ]
    dp[0][0], dp[1][0] = numbers[0][0], numbers[1][0]

    for i in range(1, n):
        for j in range(2):
            dp[j][i] = max(dp[j][i], dp[1-j][i-1]) + numbers[j][i]
            if i-2 >= 0 : dp[j][i] = max(dp[j][i], dp[1-j][i-2]+ numbers[j][i]) 
    print(max(dp[0][-1], dp[1][-1]))