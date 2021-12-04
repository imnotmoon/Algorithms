# baekjoon 9084

import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
  N = int(input())
  costs = list(map(int, input().split()))
  M = int(input())
  dp = [ 1 if idx == 0 else 0 for idx in range(M+1) ]
  for i in costs:
    for j in range(1, M+1):
      if j-i >= 0: dp[j] += dp[j-i]
  print(dp[-1])

