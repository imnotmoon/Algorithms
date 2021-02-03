# baekjoon 17836
import sys
input = sys.stdin.readline
from collections import deque

n, m, t = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
gram = 0

# bfs
def bfs():
    global gram
    queue = deque()
    queue.append((0,0))   # y, x

    while queue:
        current = queue.popleft()

        if castle[current[0]][current[1]] == 2:
            # print("gram")
            gram = visited[current[0]][current[1]]-1 + (n-1)-current[0] + (m-1)-current[1]

        for i in range(4):
            cy, cx = current[0]+dy[i], current[1]+dx[i]
            if (0<=cy<n) and (0<=cx<m) and visited[cy][cx] == 0 and castle[cy][cx] != 1:
                if visited[cy][cx] == 0:
                    queue.append((cy,cx))
                    visited[cy][cx] = visited[current[0]][current[1]]+1

visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
bfs()
# print(visited[n-1][m-1]-1, gram)
if gram > 0 :
    if visited[n-1][m-1] > 0:
        res = min(visited[n-1][m-1]-1, gram)
        print("Fail" if res > t else res)
    else :
        print("Fail" if gram > t else gram)
else :
    if visited[n-1][m-1] > 0:
        print("Fail" if visited[n-1][m-1]-1 > t else visited[n-1][m-1])
    else :
        print("Fail")        
