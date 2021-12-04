# baekjoon 2294

import sys
input = sys.stdin.readline
INF = sys.maxsize

n, k = map(int, input().split())
values = []
for i in range(n):
  values.append(int(input()))
values = list(set(values))

dp = [ 0 if i == 0 else INF for i in range(k+1) ]
for i in range(len(values)):
  for j in range(1, k+1):
    if j >= values[i]: dp[j] = min(dp[j], dp[j-values[i]]+1)

print(dp[-1] if dp[-1] < INF else -1)