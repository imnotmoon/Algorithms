# 백준 2839
# 2020 python

def main() :
    n = int(input())
    div = int(n/5)
    while(div>=0) :
        if (n-div*5)%3 == 0:
            print(div + int((n-(div*5))/3))
            return
        else:
            div -= 1
    print(-1)


if __name__ == "__main__":
    main()