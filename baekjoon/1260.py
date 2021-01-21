from sys import stdin
input = stdin.readline

f = list(map(int, input().split()))
n = f[0]; m = f[1]; v = f[2];

def dfs(v) :
    visited = [False] * (n+1)
    stack = []
    stack.append(v)
    res = ""

    while(stack):
        current = stack.pop(-1)
        if visited[current] is False:
            visited[current] = True
            res = res + str(current) + " "
            tmp = []
            for i in node[current]:
                if visited[i] is False:
                    try:
                        stack.remove(i)
                    except:
                        pass
                    tmp.append(i)
            tmp.reverse()
        stack = stack + tmp
    print(res)


def bfs(v) :
    visited = [False] * (n+1)
    queue = []
    queue.append(v)
    res = ""
    
    while(queue):
        current = queue.pop(0)
        if visited[current] is False:
            visited[current] = True
            res = res + str(current) + " "
            tmp = []
            for i in node[current]:
                if visited[i] is False and i not in queue:
                    queue.append(i)
    print(res)

node = [[] for i in range(n+1)]
edge = []
for i in range(m):
    tmp = tuple(map(int, input().split()))
    node[tmp[0]].append(tmp[1])
    node[tmp[1]].append(tmp[0])

for l in node:
    l.sort()
    
dfs(v)
bfs(v)