# baekjoon 2751
# mergeSort

import sys
input = sys.stdin.readline

n = int(input())
arr = []
sorted_array = [0] * n

def merge(s, middle, e):
    # left : s ~ middle
    # right : middle+1 ~ e
    i = s
    j = middle+1
    k = s

    while(i<=middle and j <= e) :
        if arr[i] <= arr[j]:
            sorted_array[k] = arr[i]
            i += 1
        else :
            sorted_array[k] = arr[j]
            j += 1
        k += 1
        
    # 남은부분 복사
    if i > middle:     # right 남은부분 복사
        while(j <= e):
            sorted_array[k] = arr[j]
            j += 1
            k += 1
    else :
        while(i <= middle):
            sorted_array[k] = arr[i]
            i += 1
            k += 1

    for idx in range(s, e+1):
        arr[idx] = sorted_array[idx]


def mergeSort(s, e):
    if s < e :
        middle = int((s+e)/2)
        mergeSort(s, middle)
        mergeSort(middle+1, e)

        merge(s, middle, e)

for i in range(n):
    arr.append(int(input()))

mergeSort(0, n-1)
for num in arr:
    print(num)
