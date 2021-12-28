# baekjoon 2470
# -99 -2 -1 4 98

import sys
input = sys.stdin.readline

N = int(input())
l = sorted(list(map(int, input().split())))
left, right = 0, N-1
delta = l[left] + l[right]
result = [l[left], l[right]]


while left < right:
  t = l[left] + l[right]
  if abs(t) < abs(delta) :
    delta = t
    result = [l[left], l[right]]
    if t == 0:
      break
  if t > 0 : right -= 1
  else : left += 1

print(*result)