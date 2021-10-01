# baekjoon 2212
from sys import stdin
input = stdin.readline

n, k = int(input()), int(input())
if(k >= n) :
    print(0)
    exit()

sensors = sorted(list(map(int, input().split())))
dist = sorted([sensors[i+1] - sensors[i] for i in range(len(sensors)-1)], reverse=True)
print(sum(dist[k-1:]))