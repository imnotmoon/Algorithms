# 18352

N, M, K, X = list(map(int, input().split()))
paths = [list(map(int, input().split())) for _ in range(M)]

queue = []
visitWithPathK = [0 for _ in range(N+1)]
queue.append(X)
while(queue) :
    if visitWithPathK[queue[0]] == K :
        break
    currentCity = queue.pop(0)
    for path in paths :
        if path[0] == currentCity and visitWithPathK[path[1]] == 0:
            queue.append(path[1])
            visitWithPathK[path[1]] = visitWithPathK[currentCity]+1

count = 0
for i in range(N+1) :
    if visitWithPathK[i] == K :
        print(i)
        count += 1
if count == 0 : 
    print(-1)
