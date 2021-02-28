# baekjoon 11052
import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
dp[1], dp[2] = cost[0], max(cost[0]*2, cost[1])


def get_cost(n):
    global dp
    if dp[n] > 0:
        return dp[n]
    else:
        for i in range(1, n):
            dp[n] = max(cost[n-1], get_cost(i)+get_cost(n-i), dp[n])
        return dp[n]


print(get_cost(n))
