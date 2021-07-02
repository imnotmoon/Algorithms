# baekjoon 1966
import sys; input = sys.stdin.readline
from collections import deque

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))

    if n == 1:
        print(1)
        continue

    queue = [(q[a], a) for a in range(len(q))]
    queue = deque(queue)

    cnt = 0
    while queue:
        cur = queue.popleft()
        if any([cur[0] < j[0] for j in queue]):
            queue.append(cur)
        else :
            if cur[1] == m :
                print(cnt+1)
            else : cnt += 1
