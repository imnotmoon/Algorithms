# baekjoon 11053

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
