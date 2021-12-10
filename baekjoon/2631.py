# baekjoon 2631
N = int(input())
c = [ int(input()) for _ in range(N) ]
dp = [ 1 for _ in range(N) ]

for i in range(1, N):
  for j in range(i): 
    if c[i] > c[j]: dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))  
