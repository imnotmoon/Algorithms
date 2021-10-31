# baekjoon 1629

A, B, C = map(int, input().split())

def dac(a, b):
  if b == 1 : return a % C
  t = dac(a, b//2)
  if b % 2 == 0 : return t * t % C
  else: return t * t * a % C

print(dac(A, B))