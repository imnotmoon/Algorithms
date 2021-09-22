# baekjoon 21608

import sys
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n = int(input())

seats = [ [ 0 for _ in range(n) ] for _ in range(n)]
likes = [0 for _ in range(n**2 + 1 )]
order = []

for i in range(n**2):
    t = list(map(int, input().split()))
    likes[t[0]] = t[1:]
    order.append(t[0])

def find_seat(like):
    # 1번과 2번 조건
    to_y, to_x = 0, 0
    max_empty, max_friend = 0, 0
    for i in range(n):
        for j in range(n):
            if seats[i][j] != 0 : continue
            empty, friend = 0, 0
            for k in range(4):
                y, x = i+dy[k], j+dx[k]
                if 0 <= y < n and 0 <= x < n:
                    if seats[y][x] == 0: empty += 1
                    if seats[y][x] in like: friend += 1
            if friend > max_friend: 
                to_y, to_x = i, j
                max_empty, max_friend = empty, friend
            elif friend == max_friend and empty > max_empty:
                to_y, to_x = i, j
                max_empty, max_friend = empty, friend
            elif friend == max_friend and empty == max_empty:
                if to_y > i : 
                    to_y, to_x = i, j
                    max_empty, max_friend = empty, friend
                elif to_y == i and to_x > j : 
                    to_y, to_x = i, j
                    max_empty, max_friend = empty, friend
    if seats[to_y][to_x] > 0 :
        for i in range(n):
            for j in range(n):
                if seats[i][j] == 0 :
                    return i, j
    return to_y, to_x

def calc_satisifaction(i, j):
    total = 0
    for k in range(4):
        if 0 <= i+dy[k] < n and 0 <= j+dx[k] < n :
            if seats[i+dy[k]][j+dx[k]] in likes[seats[i][j]]:
                total += 1
    return 10**(total-1 if total > 0 else 0)

for o in order:
    idx, like = o, likes[o]
    y, x = find_seat(like)
    seats[y][x] = idx

answer = 0
for i in range(n):
    for j in range(n):
        answer += calc_satisifaction(i, j)
        
print(answer)