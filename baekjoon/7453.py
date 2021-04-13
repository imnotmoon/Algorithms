# baekjoon 7453 합이 0인 네 정수

n = int(input())
A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

A.sort()
B.sort()
C.sort()
D.sort()

print(A)
print(B)
print(C)
print(D)
