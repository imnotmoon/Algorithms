# baekjoon 2644
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
start, end = tuple(map(int, input().split()))
m = int(input())
arr = [[] for _ in range(n+1)]
for i in range(m):
    tmp = tuple(map(int, input().split()))
    arr[tmp[0]].append(tmp[1])
    arr[tmp[1]].append(tmp[0])

# bfs
queue = deque()
queue.append(start)
visited = [-1 for _ in range(n+1)]
visited[start] = 0

while(queue):
    current = queue.popleft()
    if current == end:
        break
    for i in arr[current]:
        if visited[i] == -1:
            queue.append(i)
            visited[i] = visited[current] + 1
            
print(visited[end])