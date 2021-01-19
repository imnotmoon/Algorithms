# baekjoon 2798
import sys
N, M = tuple(map(int, input().split()))
cards = list(map(int, sys.stdin.readline().split()))

gap = 300000
result = 0
for i in range(len(cards)):
    for j in range(len(cards)):
        if i == j:
            continue
        for k in range(len(cards)):
            if k == j or k == i :
                continue
            total = cards[i] + cards[j] + cards[k]
            if gap > M-total and total <= M:
                gap = M-total
                result = total

print(result)