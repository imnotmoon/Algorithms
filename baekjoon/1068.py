# baekjoon 1068
from sys import stdin
from collections import deque
input = stdin.readline
n = int(input())
nodes = list(map(int, input().split()))
delete = int(input())
root = 0

graph = [[] for _ in range(n)]
for i in range(len(nodes)):
    if nodes[i] > -1 and i != delete: 
        graph[nodes[i]].append(i)
    if nodes[i] == -1:
        root = i

# bfs : graph[i] == []면 리프노드
queue = deque()

queue.append(root)
count = 0
while(queue):
    current = queue.popleft()
    if len(graph[current]) == 0:
        count += 1
        continue
    for node in graph[current]:
        if delete != node:
            queue.append(node)
if root == delete:
    print(0)
else :
    print(count)

            