def solution(maps, p, r):
    answer = 0

    for i in range(len(maps)):
        for j in range(len(maps)):
            answer = max(answer, kill_monsters(i,j, r, map))



    return answer

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
from collections import deque

def kill_monsters(y, x, r, map):
    # 노란 범위
    count = 0
    queue = deque()
    queue.push((y,x))
    visited = [[False for _ in range(len(map))] for _ in range(len(map))]
    visited[y][x] = True
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            yy, xx = cy+dy[i], cx+dx[i]
            if (0 <= yy < len(map)) and (0 <= xx < len(map)) and visited[yy][xx] is False:
                if abs(yy-y)+




solution([[1, 28, 41, 22, 25, 79, 4], 
    [39, 20, 10, 17, 19, 18, 8], 
    [21, 4, 13, 12, 9, 29, 19],
    [58, 1, 20, 5, 8, 16, 9], 
    [5, 6, 15, 2, 39, 8, 29],
    [39, 7, 17, 5, 4, 49, 5], 
    [74, 46, 8, 11, 25, 2, 11]], 19, 6)