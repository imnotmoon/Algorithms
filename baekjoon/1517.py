# baekjoon 1517
from sys import stdin
input = stdin.readline
 
n = int(input())
arr = list(map(int, input().split()))
result = [0 for _ in range(n)]
ans, cnt = 0, 0
 
def merge(start, mid, end):
    global cnt, arr
    l, r, s = start, mid+1, start
    while(l<=r and r<=end):
        if arr[l] <= arr[r]:
            result[s] = arr[l]
            l += 1
        else:
            result[s] = arr[r]
            r += 1
            cnt = cnt + mid-l+1
        s += 1
        # 남은 데이터
    if l > mid:
        while(r <= end) : 
            result[s] = arr[r]
            s += 1
            r += 1
    else:
        while(l <= mid) : 
            result[s] = arr[l]
            s += 1
            l += 1
 
    # 원래 배열로 이동
    for i in range(start, end+1):
        arr[i] = result[i]
 
def mergeSort(start, end):
    if start < end:
        mid = int((start + end) / 2)
        mergeSort(start, mid)
        mergeSort(mid+1, end)
        merge(start, mid, end)
 
mergeSort(0, n-1)
print(cnt)