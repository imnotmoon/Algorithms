# baekjoon 20040

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lines = []
for i in range(1, M+1): lines.append(list(map(int, input().split())))

parent = [ i for i in range(N) ]

def find(n):
  if n == parent[n]: return n
  else :
    parent[n] = find(parent[n])
    return parent[n]

def union(x, y):
  px, py = find(x), find(y)
  if px == py : return True
  else :
    parent[max(px, py)] = min(px, py)
    return False

ans = 0
for i in range(1, M+1):
  if union(*lines[i-1]):
    ans = i
    break
print(ans)