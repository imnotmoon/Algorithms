def solution(numbers):
    res = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            res.add(numbers[i]+numbers[j])
    answer = sorted(list(res))
    return answer


solution([2, 1, 3, 4, 1])
