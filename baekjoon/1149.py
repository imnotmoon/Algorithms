# baekjoon 1149

import sys
input = sys.stdin.readline

n = int(input())
house = []
for i in range(n):
    house.append(list(map(int, input().split())))

dp1, dp2, dp3 = [0 for _ in range(
    n+1)], [0 for _ in range(n+1)], [0 for _ in range(n+1)]
dp1[1], dp2[1], dp3[1] = house[0][0], house[0][1], house[0][2]
for i in range(2, n+1):
    dp1[i] = min(dp2[i-1]+house[i-1][0], dp3[i-1]+house[i-1][0])
    dp2[i] = min(dp1[i-1]+house[i-1][1], dp3[i-1]+house[i-1][1])
    dp3[i] = min(dp1[i-1]+house[i-1][2], dp2[i-1]+house[i-1][2])

print(min(dp1[n], dp2[n], dp3[n]))
