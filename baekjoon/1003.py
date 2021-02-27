# baekjoon 1003

t = int(input())
dp = [0 for i in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]


def fib(n):
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    if dp[n] == 0:
        minus_one, minus_two = fib(n-1), fib(n-2)
        dp[n] = [minus_one[0]+minus_two[0], minus_one[1]+minus_two[1]]
    return dp[n]


for i in range(t):
    n = int(input())
    res = fib(n)
    print(res[0], res[1])
