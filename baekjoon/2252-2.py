# baekjoon 2252 - 2

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = dict([[i, 0] for i in range(1, n+1)])
connections = [[] for i in range(0, n+1)]

for i in range(1, m+1):
    # a -> b
    a, b = map(int, input().split())
    connections[a].append(b)
    in_degree[b] += 1

queue = deque()
result = []

# 큐에 진입차수가 0인 노드 삽입
for i in range(1, n+1):
    if in_degree[i] == 0 : queue.append(i)

while queue:
    front = queue.popleft()
    result.append(front)
    for i in connections[front]:
        in_degree[i] -= 1
        if in_degree[i] == 0 : queue.append(i)

print(result)
