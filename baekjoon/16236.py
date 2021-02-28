# baekjoon 16236
from collections import deque
import sys
import copy
input = sys.stdin.readline

n = int(input())
aquarium = []
for i in range(n):
    aquarium.append(list(map(int, input().split())))

dy, dx = [-1, 0, 0, 1], [0, -1, 1, 0]


total_dist = 0
shark_size = 2
fish_eaten = 0
visited = [[False for _ in range(n)] for _ in range(n)]


def bfs(pos, fish_size):
    global total_dist, shark_size, fish_eaten
    # print(f"now : {pos}")
    aquarium[pos[0]][pos[1]] = 0
    queue = deque()
    queue.append([pos[0], pos[1], 0])
    _visited = copy.deepcopy(visited)
    eat = []
    while queue:
        current = queue.popleft()
        # print(
        #     f"  current : {current},   find for : {fish_size},    shark size : {shark_size},   fish eaten : {fish_eaten},  dist : {total_dist}")
        for i in range(4):
            move = [current[0]+dy[i], current[1]+dx[i]]
            if (0 <= move[0] < n) and (0 <= move[1] < n) and _visited[move[0]][move[1]] is False:
                if 0 < aquarium[move[0]][move[1]] <= fish_size:
                    # 물고기 먹으러 이동 가능 -> 여기를 시작으로 다시 bfs
                    dist = current[2]+1
                    eat.append([move[0], move[1], dist])
                    _visited[move[0]][move[1]] = True
                else:
                    # 상어 크기보다 크면 이동도 불가능
                    if aquarium[move[0]][move[1]] <= shark_size:
                        # 큐에 넣고 이동
                        queue.append([move[0], move[1], current[2]+1])
                        _visited[move[0]][move[1]] = True

    if len(eat) == 0:
        return total_dist
    else:
        eat.sort(key=lambda x: (x[2], x[0], x[1]))
        to = eat[0]
        total_dist += to[2]
        if fish_eaten+1 == shark_size:
            fish_eaten = 0
            shark_size += 1
            return bfs([to[0], to[1]], fish_size+1)
        else:
            fish_eaten += 1
            return bfs([to[0], to[1]], fish_size)


start = [0, 0]
for i in range(n):
    for j in range(n):
        if aquarium[i][j] == 9:
            aquarium[i][j] = 0
            shark = [i, j]
print(bfs(shark, shark_size-1))
