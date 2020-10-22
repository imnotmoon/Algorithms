from collections import Counter

# INPUT
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

#  부분합 구함
aSum = []
bSum = []
for i in range(n):
    tmp = A[i]
    aSum.append(tmp)
    for j in range(i+1, n):
        tmp += A[j]
        aSum.append(tmp)

for i in range(m):
    tmp = B[i]
    bSum.append(tmp)
    for j in range(i+1, m):
        tmp += B[j]
        bSum.append(tmp)

total = 0
c = Counter(bSum)
count = 0
for i in aSum :
    count += c[T-i]

print(count)