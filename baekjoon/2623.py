# baekjoon 2623
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = dict([i, 0] for i in range(1, n+1))
connections = [[] for _ in range(n+1)]
result = []

for i in range(m):
    list_input = list(map(int, input().split()))

    for j in range(1, len(list_input)-1):
        # 진입차수 세팅
        in_degree[list_input[j+1]] += 1
        # a -> b 연결정보 세팅
        connections[list_input[j]].append(list_input[j+1])
    
queue = deque()
for i in range(1, n+1):
    if in_degree[i] == 0 : queue.append(i)

while queue:
    front = queue.popleft()
    result.append(front)
    for i in connections[front]:
        in_degree[i] -= 1
        if in_degree[i] == 0 : queue.append(i)
    
if len(result) == n : 
    for num in result : print(num)
else : print(0)