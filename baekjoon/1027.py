# baekjoon 1027

import sys
N = int(input())
bd = list(map(int, input().split()))
sight = []
result = 0

for i in range(len(bd)):
  total = 0
  for j in range(len(bd)):  # i에서 j 빌딩이 보이는지?
    if i == j : continue
    a = (bd[i]-bd[j]) / (i-j) # i-j의 기울기
    if i < j:
      b = -sys.maxsize
      for k in range(i+1, j):
        b = max(b, (bd[k]-bd[i]) / (k-i))
      if b < a: total += 1
    if i > j:
      b = sys.maxsize
      for k in range(j+1, i):
        b = min(b, (bd[k]-bd[i]) / (k-i))
      if b > a: total += 1
  sight.append(total)

print(max(sight))