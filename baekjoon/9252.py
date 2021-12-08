# baekjoon 9252

import sys
input = sys.stdin.readline
a, b = input().rstrip(), input().rstrip()
dp = [ [0 for _ in range(len(a)+1)] for _ in range(len(b)+1) ]

for i in range(1, len(b)+1):
  for j in range(1, len(a)+1):
    if a[j-1] == b[i-1]: dp[i][j] = dp[i-1][j-1]+1
    else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ''
x, y = len(a), len(b)
while x > 0 and y > 0:
  if dp[y-1][x] == dp[y][x]: y -= 1
  elif dp[y][x-1] == dp[y][x]: x -= 1
  else:
    ans = a[x-1]+ans
    x, y = x-1, y-1

print(dp[-1][-1])
print(ans)