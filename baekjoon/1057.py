# baekjoon 1057
import math

N, K, I = map(int, input().split())
rounds = [ [] for _ in range(math.ceil(math.log2(N))+1) ]
rounds[0] = list(range(1, N+1))
rounds[0][K-1], rounds[0][I-1] = 'x', 'x'

for r in range(len(rounds)):
  for i in range(len(rounds[r])):
    if i%2 == 1: continue

    if i == len(rounds[r])-1:
      rounds[r+1].append(rounds[r][i])
      continue

    a, b = rounds[r][i], rounds[r][i+1]
    if a == 'x' and b == 'x':
      print(r+1)
      exit(0)
    if 'x' in [a, b]:
      rounds[r+1].append('x')
      continue
    if r != len(rounds)-1 : rounds[r+1].append(a)