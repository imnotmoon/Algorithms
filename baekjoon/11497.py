# baekjoon 11497.py
# 정렬 -> left, right 인덱스 각각 따로두고 정렬된 배열의 인덱스 기준 2칸씩 뛰면서 삽입

T = int(input())
arrays = []
for i in range(T):
    _ = input()
    arrays.append(sorted(list(map(int, input().split()))))

for case in arrays:
    result = []
    result.append(case[0])
    index_left = 1
    index_right = 2
    end = len(case)
    while(True):
        #left
        if index_left < end:
            result.insert(0, case[index_left])
            index_left += 2
        #right
        if index_right < end:
            result.append(case[index_right])
            index_right += 2
        if index_left >= end and index_right >= end:
            break

    diff = 0
    for i in range(end-1):
        diff = max(diff, abs(result[i]-result[i+1]))
    diff = max(diff, result[0]-result[end-1])
    print(diff)