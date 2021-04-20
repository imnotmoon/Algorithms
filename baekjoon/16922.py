# baekjoon 16922

n = int(input())
numbers = set()

for i in range(n+1):
    for j in range(n+1-i):
        for k in range(n+1-i-j):
            l = n-i-j-k
            # print(i, j, k, l)
            numbers.add(i*1 + j*5 + k*10 + l*50)

print(len(numbers))

# 최대 20^3 시간복잡도이다. 마지막꺼는 그냥 빼니까 무조건 1임 그래서 20^4가 아니다.
