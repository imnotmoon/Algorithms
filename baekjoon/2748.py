n = int(input())
dp = [ 0 for _ in range(91) ]
dp[1] = 1

def fibonacci(n):
  if n == 1:
    return 1
  if n == 0 :
    return 0
  if dp[n] > 0 :
    return dp[n]
  else :
    dp[n] = fibonacci(n-1) + fibonacci(n-2)
    return dp[n]

fibonacci(n)
print(dp[n])