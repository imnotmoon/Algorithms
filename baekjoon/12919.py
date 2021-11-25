# baekjoon 12919
S, T = input(), input()

def find(t):
  if len(t) < len(S): return
  if t == S:
    print(1)
    exit(0)
  if t[-1] == 'A': find(t[:-1])
  if t[0] == 'B': find(t[1:][::-1])

find(T)
print(0)