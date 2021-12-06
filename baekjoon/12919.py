# baekjoon 12919

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

S, T = input().rstrip(), input().rstrip()

def reverse(s):
  t = ''
  for i in s:
    t = i + t
  return t

def find(t):
  if len(t) < len(S): return
  if t == S:
    print(1)
    exit(0)
  if t[-1] == 'A': find(t[:-1])
  if t[0] == 'B': find(reverse(t[1:]))

find(T)
print(0)