# baekjoon 9019

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
tc = []
dslr = ["D", "S", "L", "R"]

for i in range(t):
    tc.append(list(map(int, input().split())))


def function_D(a):
    return 2*a % 10000


def function_S(a):
    return 9999 if a == 0 else a-1


def function_L(a):
    return (a % 1000) * 10 + (a // 1000)


def function_R(a):
    return ((a % 10) * 1000) + (a // 10)


def bfs(a, b):
    queue = deque()
    queue.append((a, ""))
    visited = [0 for _ in range(10000)]
    visited[a] = 1
    while queue:
        current = queue.popleft()
        tmp = [function_D(current[0]), function_S(current[0]),
               function_L(current[0]), function_R(current[0])]
        for i in range(4):
            if tmp[i] == b:
                return current[1] + dslr[i]
            if visited[tmp[i]] == 0:
                queue.append((tmp[i], current[1]+dslr[i]))
                visited[tmp[i]] = 1


for case in tc:
    a, b = case[0], case[1]
    res = bfs(a, b)
    print(res)
