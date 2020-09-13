n = int(input())
numbers = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = numbers[0]

for i in range(n) :
    if i == 0:
        continue
    dp[i] = max(dp[i-1]+numbers[i], numbers[i])
# print(dp)
print(max(dp))