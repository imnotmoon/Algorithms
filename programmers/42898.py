def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[n-1][m-1] = 1
    for pud in puddles: dp[pud[1]-1][pud[0]-1] = -1
    dfs(0, 0, dp)
    return dp[0][0]


def dfs(y, x, dp):
    if dp[y][x] < 0: return 0
    if dp[y][x] > 0: return dp[y][x]

    t = 0
    if y+1 < len(dp):
        t = (t + dfs(y+1, x, dp)) % 1000000007
    if x+1 < len(dp[0]):
        t = (t + dfs(y, x+1, dp)) % 1000000007
    dp[y][x] = t
    return dp[y][x]


print(solution(100, 150, [[2,2], [3, 4], [5, 7], [31, 11], [34, 56]]))