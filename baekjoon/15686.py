# baekjoon 15686

import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
city, chickens, homes = [ list(map(int, input().split())) for _ in range(N) ], [], []

for i in range(N): 
  for j in range(N) :
    if city[i][j] == 2: chickens.append((i, j))
    if city[i][j] == 1: homes.append((i, j))

picks = list(combinations(chickens, M))
result = [0] * len(picks)

for i in homes:
  for j in range(len(picks)):
    a = N+N
    for k in picks[j]:
      a = min(abs(i[0]-k[0]) + abs(i[1]-k[1]), a)  # 각 집에 대해 치킨집들을 순회 -> 가장 가까운 치킨집 구함
    result[j] += a

print(min(result))