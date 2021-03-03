# baekjoon 11501
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    max_price = 0
    total = 0
    for i in range(n-1, -1, -1):
        max_price = max(max_price, price[i])
        if price[i] < max_price:
            total += (max_price - price[i])

    print(total)
