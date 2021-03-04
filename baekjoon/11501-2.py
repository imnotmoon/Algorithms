# baekjoon 11501

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))

    total, max_cost = 0, 0
    for j in range(n-1, -1, -1):
        max_cost = max(max_cost, stocks[j])
        total += (max_cost - stocks[j])

    print(total)
