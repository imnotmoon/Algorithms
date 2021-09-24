# baekjoon  10942

import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline
n = int(input())
palindrome = list(map(int, input().split()))
m = int(input())

dp = [[-1 for _ in range(n)] for _ in range(n)]

def is_palindrome(i,j):
    global dp
    if dp[i][j] > -1 : return dp[i][j]
    if j == i:
        dp[i][j] = 1
    elif j-i == 1:
        dp[i][j] = 1 if palindrome[i] == palindrome[j] else 0
    else:
        dp[i][j] = 1 if palindrome[i] == palindrome[j] and is_palindrome(i+1, j-1) else 0
    return dp[i][j]

for i in range(n):
    for j in range(i, n):
        is_palindrome(i, j)

for i in range(m):
    a, b = map(int, input().split())
    print(is_palindrome(a-1, b-1))