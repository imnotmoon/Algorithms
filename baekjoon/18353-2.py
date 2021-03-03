# beakjoon 18353 다시풀기

n = int(input())
soldiers = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(0, i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
