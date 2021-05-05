dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

def solution(board):
    result = []
    from collections import deque
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0 : board[i][j] = 10000000
    q = deque()
    q.append((0, 0, 0, -1))
    board[0][0] = 0
    while q :
        y, x, cost, head = q.popleft()
        if (y, x) == (len(board)-1, len(board)-1):
            result.append(cost)
            continue
        for i in range(4):
            yy, xx = y+dy[i], x+dx[i]
            next_cost = cost+100 if head == i else cost+600
            if (0 <= yy < len(board)) and (0 <= xx < len(board)) and board[yy][xx] >= next_cost and board[yy][xx] != 1:
                board[yy][xx] = min(board[yy][xx], next_cost)
                q.append((yy, xx, next_cost, i))


    # for i in board:
    #     print(i)
    print(min(result)-500)
    return min(result)-500

# solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
# solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
# solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])