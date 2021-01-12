arr = list()

def input_num() :
    N = int(input())
    for i in range(N):
        arr.append(int(input()))

input_num()

# 1. 선택 정렬
def selection_sort():
    index = 0
    for i in range(len(arr)):
        min = 1001
        for j in range(i, len(arr)):
            if min > arr[j]:
                min = arr[j]
                index = j
        arr[index], arr[i] = arr[i], arr[index]
        print(arr)

# 2. 버블 정렬
def bubble_sort():
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)

# 3. 삽입 정렬
def insertion_sort():
    for i in range(len(arr)-1):
        j = i
        while(arr[j+1] < arr[j] and j >= 0):
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
        print(arr)

# 4. 퀵 정렬
def quick_sort(start, end):
    print(start, end)
    if start >= end:
        return
    if start + 1 == end:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
            return
    pivot = start
    i = start + 1
    j = end
    while(i < j):
        while(arr[pivot] >= arr[i] and i < end):
            i += 1
            if i == end:
                i = pivot
                break
        while(arr[pivot] <= arr[j] and j > start) :
            j -= 1
        if i > j:
            arr[j], arr[pivot] = arr[pivot], arr[j]
        else :
            arr[i], arr[j] = arr[j], arr[i]
        print(arr)
        
    quick_sort(start, j-1)
    quick_sort(j+1, end)

quick_sort(0, len(arr)-1)
print(arr)