manhattan = [[1, 0], [-1, 0], [0, 1], [0, -1]]
from collections import deque

def solution(places):
    answer = []
    for room in places:
        ret = True
        for row in range(len(room)):
            if ret is False:
                break
            for col in range(len(room[row])):
                if room[row][col] == 'P':
                    if get_distance(row, col, room) is False :
                        ret = False
                        break
        if ret:
            answer.append(1)
        else :
            answer.append(0)

    print(answer)
    return answer

def get_distance(y, x, room):
    print(y, x)
    queue = deque()
    queue.append([y, x])
    visited = [[0 for _ in range(5)] for _ in range(5)]
    visited[y][x] = 1
    while queue:
        current = queue.popleft()
        for m in manhattan:
            yy, xx = current[0]+m[0], current[1]+m[1]
            if (0<=yy<5) and (0 <= xx < 5) and room[yy][xx] != 'X' and visited[yy][xx] == 0:
                if(abs(yy-y)+abs(xx-x) <= 2) :
                    print("  ", room[yy][xx], yy, xx, "   dist : ", abs(yy-y)+abs(xx-x))
                    if room[yy][xx] == 'P':
                        print("  ", "False")
                        return False
                    queue.append([yy,xx])
                    visited[yy][xx] = 1
    return True




solution([
    # ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    # ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
    # ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    # ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ["PXPXP", "XPXPO", "PXPXP", "XPXPX", "PXPXP"]
    ])