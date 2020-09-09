# 1년 전 시간초과 났던거

몇번째 순서에 갔는지 등등을 visisted로 저장할 수 있음 <- dp의 memoization과 병행



m, n = tuple(map(int, input().split()))
_map = [list(map(int, input().split())) for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

start = (0, 0)
dp = [[0 for col in range(n)] for row in range(m)]
dp[0][0] = 1

for i in range(m):
    for j in range(n) :
        count = dp[i][j]
        for k in range(4) :
            if i+dy[k] >= 0 and i+dy[k] < m and j+dx[k] >= 0 and j+dx[k] < n :
                if(_map[i+dy[k]][j+dx[k]] > _map[i][j]) :
                    count += dp[i+dy[k]][j+dx[k]]
        dp[i][j] = count
for i in range(m):
    for j in range(n) :
        count = 0
        for k in range(4) :
            if i+dy[k] >= 0 and i+dy[k] < m and j+dx[k] >= 0 and j+dx[k] < n :
                if(_map[i+dy[k]][j+dx[k]] > _map[i][j]) :
                    count += dp[i+dy[k]][j+dx[k]]
        dp[i][j] = max(dp[i][j], count)

print(dp)

print(dp[m-1][n-1])

# while queue :
#     # print(queue)
#     now = queue.pop(0)
#     # print(now)
#     for i in range(4) :
#         # 경계 내에 있을 경우
#         if now[0]+dy[i] >= 0 and now[0]+dy[i] < m and now[1]+dx[i]>=0 and now[1]+dx[i] < n :
#             # 지금 칸보다 작은 값일 경우
#             if _map[now[0]][now[1]] > _map[now[0]+dy[i]][now[1]+dx[i]] :
#                 # 큐에 추가
#                 if now[0]+dy[i] == m-1 and now[1]+dx[i] == n-1 :
#                     print(_map[m-1][n-1])
#                     count += 1
#                     continue
#                 else :
#                     queue.append((now[0]+dy[i], now[1]+dx[i]))
# print(count)