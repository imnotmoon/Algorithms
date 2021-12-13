# baekjoon 14916

N = int(input())

dp = [ float('inf') for _ in range(N+1) ]
dp[0] = 0
for i in range(2, N+1):
    if i >= 5: dp[i] = min(dp[i-2], dp[i-5])+1
    else: dp[i] = -1 if dp[i-2] < 0 else dp[i-2]+1

print(dp)

print(dp[-1] if dp[-1] != float('inf') else -1)