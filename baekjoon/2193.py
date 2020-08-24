# 백준 2193.py

cnt_zeros = []

def dp_fibonacci(x) :
    global cnt_zeros
    if cnt_zeros[x] != 0 :
        return cnt_zeros[x]
    else :
        cnt_zeros[x] = dp_fibonacci(x-1) + dp_fibonacci(x-2)
        return cnt_zeros[x]


def main() :
    n = int(input())
    global cnt_zeros
    cnt_zeros = [0 for _ in range(n+1)]
    if n == 1 or n == 2 :
        print(1)
        return
    cnt_zeros[2] = 1
    cnt_zeros[3] = 1

    if n > 3 :
        for i in range(4, n+1) :
            dp_fibonacci(i)

    print(cnt_zeros[n]+cnt_zeros[n-1])



if __name__ == "__main__":
    main()