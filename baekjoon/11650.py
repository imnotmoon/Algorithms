# 11650.py
from sys import stdin
input = stdin.readline

n = int(input())
p = list()
for i in range(n):
    p.append(tuple(map(int, input().split())))

sorted_p = sorted(p, key=lambda x : (x[0], x[1]))
for i in sorted_p:
    print(i[0], i[1])