# 7 12 10 10
# 20 13 10
# 23 21
# 30

from copy import deepcopy

dp = []
pyramid = []

def get_top_value(size) :
    global dp, pyramid
    for i in range(size-1) :
        for j in range(i+1) :
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + pyramid[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + pyramid[i+1][j+1])
    

def main() :
    size = int(input())
    list_size = size*(size-1) + 1
    global dp, pyramid
    for i in range(size) :
        array = list(map(int, input().split()))
        dp.append(array)
        pyramid.append(deepcopy(array))
    
    get_top_value(size)
    print(max(dp[size-1]))
            
if __name__ == "__main__":
    main()