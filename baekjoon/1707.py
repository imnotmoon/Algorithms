# baekjoon 1707
from sys import stdin
input = stdin.readline

# 입력
K = int(input())
V, E = [], []
edges = []
for k in range(K):
    v, e = tuple(map(int, input().split()))
    V.append(v); E.append(e)
    tmp = [[] for _ in range(v+1)]
    for e in range(E[k]):
        t = tuple(map(int, input().split()))
        tmp[t[0]].append(t[1])
        tmp[t[1]].append(t[0])
    edges.append(tmp)

# BFS
def bfs(i):     # i번 노드에 대해 탐색
    global color
    queue = []
    queue.append(i)
    color[i] = 0
    while(queue):
        current = queue.pop(0)
        col = color[current]
        for node in edges[k][current]:
            if col == color[node]:
                return 0
            if color[node] == -1:
                color[node] = (col+1)%2
                queue.append(node)
    return 1
        
color = []

# 아직 탐색안함 -1 / red 0 / black 1
for k in range(K):
    # 각 정점에 대해서 bfs -> red / black
    color = [-1 for _ in edges[k]]
    total = 0
    for i in range(1, len(edges[k])):
        if edges[k][i] :
            if color[i] == -1 :
                if bfs(i) == 0:
                    print("NO")
                    break
        if i == len(edges[k])-1:
            print("YES")