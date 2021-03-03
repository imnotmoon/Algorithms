# beakjoon 3190
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())    # 보드 크기
k = int(input())    # 사과 개수
apples = []         # 사과 위치가 저장된 배열
drift = []          # 방향 전환하는 위치가 저장된 배열
for i in range(k):
    apples.append(list(map(int, input().strip().split())))
l = int(input())
for i in range(l):
    drift.append(list(map(str, input().strip().split())))

snake = deque()
snake.append([0, 0])
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
d = 0
count = 0
while(True):
    head = snake[0]
    # 이동하려는 칸이 벽일 경우 종료
    if (0 > head[0]+dy[d]) or (n <= head[0]+dy[d]) or (0 > head[1]+dx[d]) or (n <= head[1]+dx[d]):
        count += 1
        break
    # 이동하른 칸에 뱀의 몸이 있을 경우 종료
    if [head[0]+dy[d], head[1]+dx[d]] in snake:
        count += 1
        break

    # move
    if [head[0]+dy[d]+1, head[1]+dx[d]+1] in apples:
        snake.appendleft([head[0]+dy[d], head[1]+dx[d]])
        count += 1
        apples.remove([head[0]+dy[d]+1, head[1]+dx[d]+1])
    else:
        snake.pop()
        snake.appendleft([head[0]+dy[d], head[1]+dx[d]])
        count += 1

    # 방향전환
    for i in drift:
        if count == int(i[0]):
            if i[1] == 'D':     # right
                d = (d+1) % 4
            elif i[1] == 'L':   # left
                d = (d+3) % 4

print(count)
