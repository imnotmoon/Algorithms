# baekjoon 1034

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lights, result = [], 0
for i in range(N):
  lights.append(input().rstrip())
K = int(input())

for r in range(len(lights)):
  t = 0
  for s in lights[r]:
    if s == '0': t+=1
  if t <= K and t%2 == K%2:
    same_row = 0
    for rr in range(len(lights)):
      if lights[r] == lights[rr]:
        same_row += 1
    result = max(result, same_row)

print(result)
  
