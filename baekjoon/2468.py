# 백준 2468
import sys
sys.setrecursionlimit(100000)
def dfs(height, startY, startX):
    # 방문한 인덱스 튜플들의 리스트
    queue = list()
    queue.append((startY,startX))
    while(queue):
        current = queue[0]
        queue.pop(0)
        for i in range(4) :
            x = current[1]+dx[i]
            y = current[0]+dy[i]
            if (0 <= x < N) and (0 <= y < N) and visited[y][x] == 0 :
                if area[y][x] > height :
                    visited[y][x] = 1
                    queue.append((y, x))

# 1. 입력
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
r = sys.stdin.readline
N = int(r())
area = [list(map(int, r().split(' '))) for _ in range(N)]
maxHeight = max(map(max, area))

# 2. 높이마다 섬 개수 비교
maxIslands = 0
visited = [[0] * N] * N

for i in range(0, maxHeight) :  # 높이마다
    visited = [[0]*N for i in range(N)]
    count = 0
    for y in range(N) :
        for x in range(N) :
            if area[y][x] > i and visited[y][x] == 0 :
                dfs(i, y, x)
                count += 1

    maxIslands = max(maxIslands, count)

print(maxIslands)