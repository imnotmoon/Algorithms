# baekjoon 2096

import sys
input = sys.stdin.readline
N = int(input())

max_dp = [ [0 for _ in range(3)] for _ in range(2) ]
min_dp = [ [0 for _ in range(3)] for _ in range(2) ]

for i in range(N):
  tmp = list(map(int, input().split()))
  for j in range(3):
    if j == 0 : 
      max_dp[1][j] = max(max_dp[0][j], max_dp[0][j+1])+tmp[j]
      min_dp[1][j] = min(min_dp[0][j], min_dp[0][j+1])+tmp[j]
    elif j == 1: 
      max_dp[1][j] = max(*max_dp[0])+tmp[j]
      min_dp[1][j] = min(*min_dp[0])+tmp[j]
    else: 
      max_dp[1][j] = max(max_dp[0][j-1], max_dp[0][j])+tmp[j]
      min_dp[1][j] = min(min_dp[0][j-1], min_dp[0][j])+tmp[j]
  max_dp, min_dp = max_dp[1:]+[[0, 0, 0]], min_dp[1:]+[[0, 0, 0]]

print(max(*max_dp[0]), min(*min_dp[0]))
