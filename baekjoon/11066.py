# baekjoon 11066

import sys
input = sys.stdin.readline

for t in range(int(input())):
  K = int(input())
  chapters = list(map(int, input().split()))
  dp = [ [0 for _ in range(K+1)] for _ in range(K+1) ]
  
  for i in range(K-1):
    dp[i][i+1] = chapters[i] + chapters[i+1]
    for j in range(i+2, K):
      dp[i][j] = dp[i][j-1] + chapters[j]
    
  for v in range(2, K):
    for i in range(K-v):
      j = i+v
      dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i, j)])

  print(dp[0][K-1])