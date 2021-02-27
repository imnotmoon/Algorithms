# baekjoon 10216 다시풀기

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
cases = []
for i in range(t):
    cases.append([])
    n = int(input())
    for j in range(n):
        cases[i].append(list(map(int, input().split())))


def is_connected(x, y):
    dist = (x[0]-y[0])**2 + (x[1]-y[1])**2
    if dist <= (x[2]+y[2])**2:
        return True
    return False


def bfs(arr, visited, start):        # start는 인덱스
    queue = deque()
    queue.append(start)
    while(queue):
        current = queue.popleft()
        visited[current] = True
        for i in range(len(arr)):
            if i != current and is_connected(arr[i], arr[current]) and visited[i] is False:
                queue.append(i)


for i in range(t):
    # bfs
    towers = cases[i]
    count = 0
    visited = [False for j in range(len(towers)+1)]
    for j in range(len(towers)):
        if visited[j] is False:
            bfs(towers, visited, j)
            count += 1
    print(count)
