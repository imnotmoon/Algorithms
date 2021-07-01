import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
population = [0] + list(map(int, input().split()))
minDelta = 10000000
total = [ i for i in range(1, n+1)]

nodes = [[] for _ in range(n+1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    if len(tmp) > 0 :
        nodes[i+1] = tmp[1:]

def checkConnected(arr):
    if len(arr) == 1 : return True
    queue = deque()
    queue.append(arr[0])
    visited = [0] * (n+1)

    while queue:
        current = queue.popleft()
        for i in nodes[current]:
            if i in arr and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
        
                if sum(visited) == len(arr) : 
                    # print("    ", visited)
                    return True

    return False

def backtracking(idx, current):
    print(idx, current)
    global minDelta
    if idx == n :
        if 0 < len(current) < n :
            A = current
            B = list(set(total) - set(A))
            if checkConnected(B) and checkConnected(A):
                sumA, sumB = sum([population[i] for i in A]), sum([population[i] for i in B])
                minDelta = min(minDelta, abs(sumA - sumB))
    else :
        # ! 백트래킹 처음보는 방법
        backtracking(idx+1, current)
        backtracking(idx+1, current+[idx+1])

backtracking(0, [])

print(minDelta if minDelta != 10000000 else -1)