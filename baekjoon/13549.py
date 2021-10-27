# baekjoon 13549
from collections import deque
n, k = map(int, input().split())
dp = [100000] * 100001

def find(n, t):
  global dp
  queue = deque()
  queue.append((n, t))
  while queue:
    num, time = queue.popleft()
    dp[num] = time
    if num == k : return
    if num*2 <= 100000 and dp[2*num] > time : queue.append((2*num, time))
    if num-1 >= 0 and dp[num-1] > time+1 : queue.append((num-1, time+1))
    if num+1 <= 100000 and dp[num+1] > time+1 : queue.append((num+1, time+1))
  
find(n, 0)
print(dp[k])