# baekjoon 11722

n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    tmp = []
    for j in range(0, i):
        if arr[j] > arr[i]:
            tmp.append(dp[j])
    if len(tmp) > 0:
        dp[i] = max(tmp) + 1

print(max(dp))
