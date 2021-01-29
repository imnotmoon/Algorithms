T = int(input())
field = []
visited = [[]]*T
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
M, N, K = [0]*T, [0]*T, [0]*T

def dfs(f, x, y):
    current_field = field[f]
    stack = []
    stack.append((x,y))
    while(stack):
        current = stack.pop(-1)
        if visited[f][current[0]][current[1]] == 0:
            visited[f][current[0]][current[1]] = 1
            for i in range(4):
                cx, cy = current[0]+dx[i], current[1]+dy[i]
                if (0<=cx<N[f]) and (0<=cy<M[f]) and visited[f][cx][cy] == 0:
                    if current_field[cx][cy] == 1:
                        stack.append((cx, cy))

for t in range(T):
    # 입력
    M[t], N[t], K[t] = tuple(map(int, input().split()))
    tmp = [[0 for _ in range(M[t])] for _ in range(N[t])]
    for k in range(K[t]):
        tup = tuple(map(int, input().split()))
        tmp[tup[1]][tup[0]] = 1

    field.append(tmp)
    visited[t] = [[0 for _ in range(M[t])] for _ in range(N[t])]

# dfs
for t in range(T):
    m, n, k = M[t], N[t], K[t]
    count = 0
    for i in range(n):
        for j in range(m):
            if field[t][i][j] == 1 and visited[t][i][j] == 0:
                dfs(t, i, j)
                count += 1
    print(count)
    