# baekjoon 2156
# 태형이가 도와줌

n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0, wine[0]]

if n > 1:
    dp.append(wine[0]+wine[1])

for i in range(3, n+1):
    # wine은 i-1이 오늘
    # dp는 i가 오늘
    # 그저께까지+오늘(어제 안먹음), 그저께까지+어제+오늘, 어제까지+오늘안먹음
    dp.append(max(dp[i-2]+wine[i-1], wine[i-1]+wine[i-2]+dp[i-3], dp[i-1]+0))

print(dp[n])
