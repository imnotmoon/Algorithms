# 백준 1463
# 2020 python

arr = []
n = 0

def dp(x) :
    global arr
    arr[x+1] = min(arr[x+1], arr[x]+1)
    if(x*2 <= n) :
        arr[x*2] = min(arr[x*2], arr[x]+1)
    if(x*3 <= n) :
        arr[x*3] = min(arr[x*3], arr[x]+1)


def main() :
    global arr, n
    n = int(input())
    arr = [99999 for _ in range(n+1)]
    arr[1] = 0
    arr[0] = 0

    for i in range(n) :
        dp(i)
        
    print(arr[n])



if __name__ == "__main__":
    main()
