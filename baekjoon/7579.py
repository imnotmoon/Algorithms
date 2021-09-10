# baekjoon 7579
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [[0 for j in range(sum(cost)+1)] for _ in range(n+1)] # cost
result = sum(cost)

for i in range(1, n+1):
    for j in range(1, sum(cost)+1):
        if cost[i-1] > j : dp[i][j] = dp[i-1][j]
        else : dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + mem[i-1])
        if dp[i][j] >= m : result = min(result, j)
        
print(result)