#  baekjoon 2662 - 다시풀기

import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
profits = [[0]]
for i in range(n):
    profits.append(list(map(int, input().split()))[1:])

ks = [profits[i][0] for i in range(n+1)]
combination = [[i] for i in range(n+1)]

for i in range(1, m):
    for j in range(n, -1, -1):
        t = 0
        for k in range(1, j+1):
            if ks[j] < ks[j-k] + profits[k][i]:
                ks[j] = ks[j-k] + profits[k][i]
                combination[j] = copy.deepcopy(combination[j-k])
                t = k
        combination[j].append(t)
        

print(ks[-1])
print(*combination[-1])
