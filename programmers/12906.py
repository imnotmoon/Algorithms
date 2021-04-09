def solution(arr):
    answer = [-1]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)

    answer.pop(0)
    return answer


solution([1, 1, 3, 3, 0, 1, 1])
solution([4, 4, 4, 3, 3])
