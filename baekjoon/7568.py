import sys; input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

ret = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j :
            if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]: cnt += 1
    ret.append(cnt)

for i in ret:
    print(i+1, end=' ')