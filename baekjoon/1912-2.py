# baekjoon 1912 소마 대비 다시풀기

import sys
import copy
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = copy.deepcopy(arr)

for i in range(1, len(arr)):
    dp[i] = max(dp[i], dp[i-1]+arr[i])

print(max(dp))
