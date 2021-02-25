# baekjoon 2559

n, k = map(int, input().split())
temp = list(map(int, input().split()))
arr = [0 for _ in range(n)]
arr[0] = sum(temp[0:k])

i, j = k, 0
while(i < n):
    arr[j+1] = arr[j] - temp[j] + temp[i]
    i += 1
    j += 1
print(max(arr[:j+1]))
