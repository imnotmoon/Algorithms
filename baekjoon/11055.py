# baekjoon 11055
# import sys
# input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    tmp = []
    for j in range(0, i):
        if arr[i] > arr[j]:
            tmp.append(dp[j]+arr[i])
    if tmp:
        dp[i] = max(tmp)
    else:
        dp[i] = arr[i]

print(dp)

print(max(dp))
