# baekjoon 22864
import sys
sys.setrecursionlimit(2**23)

A, B, C, M = map(int, input().split())
result = 0
def w(t, burn, work):
  if burn < 0 : burn = 0
  if t == 24:
    global result
    result = max(result, work)
    return
  global A, B, C, M
  if burn+A <= M : 
    w(t+1, burn+A, work+B)
    if burn != 0 : w(t+1, burn-C, work)
  else :
    w(t+1, burn-C, work)

w(0, 0, 0)
print(result)