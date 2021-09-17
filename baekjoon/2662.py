# baekjoon 2662
import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
profits = [[0, 0]]
for i in range(n):
    profits.append(list(map(int, input().split()))[1:])

ks = [profits[i][0] for i in range(n+1)]
combnation = [[i] for i in range(n+1)]

for i in range(1, m):
    for j in range(n, -1, -1):
        temp = 0
        for k in range(1, j+1):
            if ks[j] <  ks[j-k]+profits[k][i]:
                ks[j] = ks[j-k] + profits[k][i]
                combnation[j] = copy.deepcopy(combnation[j-k])
                temp = k
        combnation[j].append(temp)

print(ks[-1])
print(*combnation[-1])
