# 2020. 10. 5.

n = input()
dp = [0]*(len(n)+1) # 동적프로그래밍. 맨 뒷칸부터 채울거
dp[len(n)-1] = 1
dp[len(n)] = 1

if len(n) == 0 :
    print(0)
    exit()

for i in range(len(n)-1, -1, -1) :
    if n[i] == '0' :
        dp[i] = 0
        continue
    else :
        dp[i] = dp[i+1]
    
    if i != len(n)-1 and int(n[i]+n[i+1]) <= 26 :
        dp[i] += dp[i+2]
    # print(i, " : ", n[i], " : ", dp[i])

print(dp[0]%1000000)



