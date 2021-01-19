# baekjoon 4963.py

dx = [1, -1, 0]
dy = [0, 1, -1]
square = []


def bfs(i, j, m, n):
    # 방문하면 -1로 바꾼다
    global sqaure
    queue = []
    queue.append((i,j))
    square[i][j] = -1
    while(queue) :
        # print(queue[0])
        current = queue.pop(0)
        for xx in dx:
            for yy in dy:
                x, y = current[0]+xx, current[1]+yy
                if (0 <= x <= n-1) and (0 <= y <= m-1) and square[x][y] == 1:
                    # print("   " + str(x), str(y))
                    square[x][y] = -1
                    queue.append((x,y))
        # print(queue)


def main(m, n) :
    global square
    square =[]
    for i in range(n) :
        square.append(list(map(int, input().split())))
    
    # dfs for every 1 island
    cnt = 0
    for i in range(n):
        for j in range(m):
            if square[i][j] == 1:
                bfs(i, j, m, n)
                cnt += 1
    return cnt

tup = tuple(map(int, input().split()))
ret =[]
while(tup != (0,0)) :
    ret.append(main(tup[0], tup[1]))
    tup = tuple(map(int, input().split()))

for r in ret:
    print(r)
