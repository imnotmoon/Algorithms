# 1697
from collections import deque
n, k = map(int, input().split())
time = [0]*100001

#bfs
queue = deque()
queue.append(n)
while queue:
    current = queue.popleft()
    if 0 < current <= 100000:
        if time[current-1] == 0 and current-1 != n:
            time[current-1] = time[current]+1
            queue.append(current-1)
    if 0 <= current <= 99999:
        if time[current+1] == 0 and current+1 != n:
            time[current+1] = time[current]+1
            queue.append(current+1)
    if current<=50000:
        if time[current*2] == 0 and current*2 != n:
            time[current*2] = time[current]+1
            queue.append(current*2)

print(time[k])
    