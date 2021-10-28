# baekjoon 16928
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
ladders, snakes = [list(map(int, input().split())) for _ in range(n)], [list(map(int, input().split())) for _ in range(m)]
board = [-1] * 101

def bfs():
  queue = deque()
  queue.append((1, 0))
  visited = [-1] * 101
  visited[1] = 0
  while queue:
    pos, dice = queue.popleft()
    if pos == 100 : return dice

    for ladder in ladders:
      if ladder[0] == pos :
        pos = ladder[1]
        break
    for snake in snakes:
      if snake[0] == pos:
        pos = snake[1]
        break
    
    for i in range(1, 7):
      if pos+i < 101 and visited[pos+i] < 0 : 
        visited[pos+i] = dice+1
        queue.append((pos+i, dice+1))

print(bfs())