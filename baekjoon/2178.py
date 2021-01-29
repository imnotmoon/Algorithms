# baekjoon 2178
from sys import stdin
from collections import deque
input = stdin.readline

n, m = tuple(map(int, input().split()))
maze = [] 
for i in range(n):
    maze.append(input())

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

# bfs
queue = deque()
visited = [[0 for _ in range(m)] for _ in range(n)]
queue.append((0,0))
visited[0][0] = 1
while(queue):
    y, x = queue.popleft()
    for i in range(4):
        cy, cx = y+dy[i], x+dx[i]
        if (0<= cy < n) and (0<= cx < m) and maze[cy][cx] == "1" and visited[cy][cx] == 0:
            queue.append((cy,cx))
            visited[cy][cx] = visited[y][x]+1
    # for i in visited:
    #     print(i)
    # print()
    
print(visited[n-1][m-1])