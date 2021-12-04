# baekjoon 2231
import sys
INF = sys.maxsize

n = int(input())
result = INF

def getInitializer(t):
  st = str(t)
  for i in range(len(st)):
    t += int(st[i])
  return t

for i in range(1, n):
  t = getInitializer(i)
  if t == n: result = min(result, i)

print(result if result != INF else 0)