# baekjoon 1517
from sys import stdin
input = stdin.readline
 
n = int(input())
arr = list(map(int, input().split()))
ans, cnt = 0, 0
result = [0 for _ in range(n)]

def merge(start, mid, end):
    global cnt, arr
    i, j, k = start, mid+1, start
    while(i<=mid and j<=end):
        if arr[i] <= arr[j]:
            result[k] = arr[i]
            i += 1
        else:
            result[k] = arr[j]
            j += 1
            cnt = cnt + mid-i+1
        k += 1

    # 남은 데이터
    if i > mid:
        while(j <= end) :
            result[k] = arr[j]
            k += 1
            j += 1
    else:
        while(i <= mid) : 
            result[k] = arr[i]
            k += 1
            i += 1
 
    # 원래 배열로 이동
    for idx in range(start, end+1):
        arr[idx] = result[idx]
 
def mergeSort(start, end):
    if start < end:
        mid = int((start + end) / 2)
        mergeSort(start, mid)
        mergeSort(mid+1, end)
        merge(start, mid, end)
 
mergeSort(0, n-1)
print(cnt)