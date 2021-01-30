# baekjoon 11333 : 점화식 + dp

t = int(input())
case = [int(input()) for _ in range(t)]
dp = [0]* 10001
mod = 1000000007

def tile_count():
    dp[0], dp[3], dp[6] = 1, 3, 13
    i = 9
    while(True):
        if i > 10000 : break
        dp[i] = int(int((5*dp[i-3])%mod) + mod - int((3*dp[i-6])%mod) + dp[i-9])%mod
        i += 3
    
tile_count()

for c in case:
    print(dp[c])