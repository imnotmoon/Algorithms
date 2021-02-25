# baekjoon 10216

import sys
import math
input = sys.stdin.readline

T = int(input())
pos = [[] for i in range(T)]
for i in range(T):
    N = int(input())
    for j in range(N):
        pos[i].append(list(map(int, input().split())))


def is_connected(x, y):
    # print(x, y)
    dx, dy = x[0]-y[0], x[1]-y[1]
    # print((dx*dx)+(dy*dy), math.pow(x[2]+y[2], 2))
    if (dx*dx)+(dy*dy) <= math.pow(x[2]+y[2], 2):
        # print("connected")
        return True
    return False


def get_parent(parents, x):
    if parents[x] == x:
        return x
    parents[x] = get_parent(parents, parents[x])
    return parents[x]


def union(parents, current_pos, a, b):
    # get distance between a and b
    root_a, root_b = get_parent(parents, a), get_parent(parents, b)
    if(root_a != root_b):
        parents[a] = root_b


for i in range(T):
    current_pos = pos[i]
    parents = [i for i in range(len(current_pos))]

    for j in range(len(current_pos)):
        for k in range(j+1, len(current_pos)):
            if is_connected(current_pos[j], current_pos[k]):
                union(parents, current_pos, j, k)

    for i in range(len(current_pos)):
        get_parent(parents, i)

    # print(parents)

    print(len(set(parents)))
