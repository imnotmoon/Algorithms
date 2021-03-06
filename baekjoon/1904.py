# baekjoon 1904

# 맨 앞자리가 0일때 : i-2 자리
# 맨 앞자리가 1일때 : i-1 자리
# 피보나치다

n = int(input())
a, b = 0, 1

for i in range(n):
    a, b = b, (a+b) % 15746

print(b % 15746)
