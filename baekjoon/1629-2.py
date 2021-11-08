# baekjoon 1629 - 다시풀기

A, B, C = map(int, input().split())

def get_modulo(b):
  if b == 1 : return A % C
  if b % 2 == 0 : return get_modulo(b//2)**2 % C
  else : return get_modulo(b//2)**2 * A % C

print(get_modulo(B))