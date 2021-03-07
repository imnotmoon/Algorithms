# baekjoon 2156 *****
n = int(input())
wines = []
for i in range(n):
    wines.append(int(input()))

dp = [0]
dp.append(wines[0])
if n > 2:
    dp.append(wines[0]+wines[1])

for i in range(3, n+1):
    case1 = wines[i-1]+dp[i-2]
    case2 = wines[i-1]+wines[i-2]+dp[i-3]
    case3 = dp[i-1]
    # print(wines, wines[i-1])
    # print("이번 포도주를 먹고 이전 포도주를 먹지 않은 경우 : ", case1)
    # print("이번 포도주를 먹고 이전 포도주도 먹은 경우 : ", case2)
    # print("이번 포도주를 먹지 말아야 하는 경우 : ", case3)

    dp.append(max(case1, case2, case3))
    # print(dp)
    # print()

print(dp[n])
