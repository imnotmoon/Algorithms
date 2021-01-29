N = int(input())
array = [input() for _ in range(N)]
array_red_to_green = [s.replace('R', 'G') for s in array]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(array, x, y, color):
    global visited
    queue = []
    queue.append((x,y))
    while(queue):
        current = queue.pop(0)
        if visited[current[0]][current[1]] == 0:
            visited[current[0]][current[1]] = 1
            for i in range(4):
                cx = current[0]+dx[i]
                cy = current[1]+dy[i]
                if (0 <= cx < N) and (0 <= cy < N):
                    if array[cx][cy] == color and visited[cx][cy] == 0:
                        queue.append((cx, cy))
            
# 적록색약이 아닌 사람
visited = [[0 for _ in range(N)] for _ in range(N)]
count = 0
for i in range(N):
    for j in range(len(array[i])):
        if visited[i][j] == 0:
            bfs(array, i, j, array[i][j])
            count += 1
print(count)

# 적록색약인 사람
visited = [[0 for _ in range(N)] for _ in range(N)]
count = 0
for i in range(N):
    for j in range(len(array[i])):
        if visited[i][j] == 0:
            bfs(array_red_to_green, i, j, array_red_to_green[i][j])
            count += 1
print(count)