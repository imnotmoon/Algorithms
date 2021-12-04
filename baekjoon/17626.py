# baekjoon 17626
import math

n = int(input())
dp = [ 4 for _ in range(n+1) ]
dp[0] = 0

for i in range(1, math.floor(math.sqrt(n))+1):
  for j in range(pow(i, 2), min(pow(i, 2)*4, n)+1):
    t = dp[j-pow(i, 2)]+1
    if dp[j] > t : dp[j] = t

print(dp[n])