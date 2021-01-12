# 선택, 버블, 삽입 정렬은 시간복잡도가 n^2이라 큰 수의 정렬에서는 사용하기 무리
# 피벗과 LEFT, RIGHT
#  '분할 정복'
# O(nlogn) : 로그는 거의 상수에 가깝게 작은 수

# 특정한 값을 기준으로 큰 숫자와 작은 숫자를 서로 교환한 후에 배열을 반으로 나눔
# 특정한 피벗 값을 기준으로 왼쪽/오른쪽으로 나눈다

# 일반적으로 맨 앞의 값을 피벗으로 설정함

# 1. 맨 앞 값을 피벗으로 지정
# 2. 왼쪽끝에서부터 피벗보다 큰 값을 선택 / 오른쪽 끝에서부터 피벗보다 작은 값을 선택
# 3. 둘이 스왑
# 4. 만약 둘이 엇갈렸다면 작은 값과 피벗을 스왑
    # => 피벗을 기준으로 왼쪽은 작고 오른쪽은 크도록 정렬된다
# 왼쪽과 오른쪽에서 각각 위 과정 반복

# 원소 하나의 정렬은 자기자신

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]


# 클린 코드를 위해 보통 재귀로 많이 작성함
def quickSort(start, end):
    print(start, end)
    global array
    if start >= end :       # 종료조건
        return
    if start+1 == end:
        if array[start] > array[end]:
            array[start], array[end] = array[end], array[start]
            return

    pivot = start
    i = start + 1   # 피벗의 바로 오른쪽 값부터 시작해서 오른쪽으로 가며 큰 값을 탐색
    j = end         # 맨 마지막 값부터 시작해서 왼쪽으로 가며 작은 값을 탐색

    while(i <= j) :     # 엇갈릴 때까지 반복
        while(array[i] <= array[pivot] and i < end):
            # print(array[i], array[pivot])
            i += 1
            if i == end:
                i = pivot
                break
        while(array[j] >= array[pivot] and j > start):
            j -= 1
        if(i > j) :     # 엇갈린 상태면 피봇과 작은걸 교차
            array[j], array[pivot] = array[pivot], array[j]
        else :
            array[j], array[i] = array[i], array[j]
        print(array)
    
    # 재귀적으로 왼쪽과 오른쪽 진행
    quickSort(start, j-1)       # LEFT
    quickSort(j+1, end)         # RIGHT

def main() :
    quickSort(0, len(array)-1)
    print(array)


if __name__ == "__main__":
    main()

# O(nlogn) 일반적인 속도
# 대수적인 경우에서는 반씩 쪼개질거라서 밑이 2인 log.

# 치명적인 약점 : 피벗값에 따라서 최악의 경우 O(n^2)
# 이미 정렬되어 있을 경우에 1보다 작은 값이 오른쪽에 없어서 결국 겨우 하나만 정렬

# 하지만 거의 대부분의 경우에서는 굉장히 빠름.
# 그래서 O(nlogn)을 요구하는 알고리즘 문제에서 퀵정렬을 이용할 경우 틀릴때가 있음