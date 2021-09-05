# baekjoon 2252

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = dict([[i+1, 0] for i in range(n)])
connections = [[] for i in range(n+1)]
result = []

for i in range(m):
    a, b = map(int, input().split())
    connections[a].append(b)
    in_degree[b] += 1

def topologySort():
    global in_degree, connections, result
    queue = deque()

    for i in range(1, n+1):
        if in_degree[i] == 0 : queue.append(i)
    
    while queue :
        front = queue.popleft()
        # result 배열에 추가
        result.append(front)
        for i in connections[front]:
            in_degree[i] -= 1
            if in_degree[i] == 0 : queue.append(i)

topologySort()

for r in result:
    print(r, end = ' ')
