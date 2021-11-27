# baekjoon 10775

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
G, P = int(input()), int(input())
gi = []
for i in range(P):
  gi.append(int(input()))

dp = [ i for i in range(G+1) ]
dock = [ 0 for _ in range(G+1) ]
ans = 0

def docking(og, num):
  if num == 0 :
    return False
  if dock[num] == 0:
    dock[num] = 1
    dp[num] -= 1
    dp[og] = dp[num]
    return True
  else :
    return docking(og, dp[num])

for i in gi:
  if docking(i, i):
    ans+=1
  else :
    print(ans)
    exit(0)
    
print(ans)