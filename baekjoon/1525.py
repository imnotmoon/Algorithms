# 1525
# dict를 사용한 visit체크와 2차원 배열의 string화

import time
import sys
from collections import deque
import copy
input = sys.stdin.readline

puzzle = ""
for i in range(3):
    puzzle += input().replace(' ', '').replace('\n', '')

zero = puzzle.find('0')

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque()
q.append(puzzle)
visited = dict()
visited[puzzle] = 0

move = -1

while q:
    current = q.popleft()
    zero = current.find('0')

    if current == '123456780':
        move = visited[current]
        break

    y, x = zero//3, zero % 3

    for i in range(4):
        current_puzzle = copy.deepcopy(current)
        cy, cx = y+dy[i], x+dx[i]
        to_swap = cy*3 + cx
        if (0 <= cy < 3) and (0 <= cx < 3):
            if zero < to_swap:
                current_puzzle = current_puzzle[:zero] + current_puzzle[to_swap] + \
                    current_puzzle[zero+1:to_swap] + \
                    current_puzzle[zero] + current_puzzle[to_swap+1:]
            else:
                current_puzzle = current_puzzle[:to_swap] + current_puzzle[zero] + \
                    current_puzzle[to_swap+1:zero] + \
                    current_puzzle[to_swap] + current_puzzle[zero+1:]

            if visited.get(current_puzzle) == None:
                q.append(current_puzzle)
                visited[current_puzzle] = visited[current] + 1

print(move)
