# baekjoon 15486

import sys; input = sys.stdin.readline

n = int(input())
length = []
price = []
for i in range(7):
    t, p = map(int, input().split())
    length.append(t)
    price.append(p)

print(length, price)