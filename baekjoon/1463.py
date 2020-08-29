# 백준 1463
# 2020 python

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

arr = []
n = 0

def dp(x) : # x는 arr상의 인덱스
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
