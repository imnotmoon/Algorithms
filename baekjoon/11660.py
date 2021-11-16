# baekjoon 11660
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
poses = [ map(int, input().split()) for _ in range(M) ]
dp = [ [0 for _ in range(N)] for _ in range(N) ]
dp[0][0] = board[0][0]

for i in range(1, N):
  dp[0][i] = dp[0][i-1]+board[0][i]
  dp[i][0] = dp[i-1][0]+board[i][0]

for i in range(1, N):
  for j in range(1, N):
    dp[i][j] = board[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for i in range(M):
  y1, x1, y2, x2 = poses[i]
  result = dp[y2-1][x2-1]
  cnt = 0
  if x1-1 > 0 :
    result = result - dp[y2-1][x1-2]
    cnt += 1
  if y1-1 > 0 :
    result = result - dp[y1-2][x2-1]
    cnt += 1
  if cnt == 2 : result += dp[y1-2][x1-2]
  print(result)