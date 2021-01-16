# MergeSort
# '분할정복' 방법을 채택 -> O(nlogn). 최악의 경우에도 보장
# 퀵정렬은 피벗값에 따라 편향되게 분할할 가능성이 있다는 점에서 O(nlogn)을 보장하지 않음

# 알단 반으로 나누고 나중에 합쳐서 정렬

# 일단 다 쪼개서 하나로 만들고 -> 하나는 그 자체로 정렬이 되어있다.
# 붙일때는 2의 배수개가 되도록 붙임
# 이미 정렬이 되어있는 상태에서 새롭게 정렬이 되어있는 큰 배열을 만듦

# 각 단계마다 처리하는 데이터의 개수가 2, 4, 8... 이라서 logN이 나옴
# 근데 딱히 퀵정렬보다 빠르지는 않으나 시간복잡도를 보장한다는 점에서 더 낫다

import sys

sorted_array = [0, 0, 0, 0, 0, 0, 0, 0]       # 정렬된 원소를 저장하는 임시 배열

def merge(array, m, middle, n):
    # i _ | j _
    # k _ _ _ _
    i = m
    j = middle + 1
    k = m

    # 작은 순서대로 배열에 삽입
    while(i <= middle and j <= n):
        if array[i] <= array[j] :
            sorted_array[k] = array[i]
            i += 1
        else :
            sorted_array[k] = array[j]
            j += 1
        k += 1

    # 남은 데이터도 삽입
    if i > middle :
        while(j <= n) :
            sorted_array[k] = array[j]
            k += 1
            j += 1
    else :
        while(i <= middle) :
            sorted_array[k] = array[i]
            k += 1
            i += 1
    
    # 원래 배열로 이동
    for idx in range(m, n+1):
        array[idx] = sorted_array[idx]


def mergeSort(array, m, n):
    if m < n :
        middle = int((m+n)/2)
        mergeSort(array, m, middle)
        mergeSort(array, middle+1, n)
        merge(array, m, middle, n)


def main():
    array = [7, 6, 5, 8, 3, 5, 9, 1]
    # print(len(array))
    mergeSort(array, 0, len(array)-1)
    print(array)


if __name__ == "__main__":
    main()