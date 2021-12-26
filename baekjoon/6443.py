# baekjoon 6443
import sys
input = sys.stdin.readline
VISITED_ALL = 0
word = ''
s = set()

def backtracking(current, v):
  if v == VISITED_ALL:
    print(current)
    return
  for i in range(len(word)):
    if v & (1 << i) == 0 and current+word[i] not in s:
      s.add(current)
      backtracking(current+word[i], v | (1 << i))

N = int(input())
for i in range(N):
  word = sorted(list(input().rstrip()))
  s = set()
  VISITED_ALL = (1 << len(word)) -1
  backtracking('', 0)
