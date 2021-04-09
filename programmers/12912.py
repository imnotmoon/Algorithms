def solution(a, b):
    answer = 0
    for i in range(min(a, b), max(a, b)+1):
        answer += i
    return answer


solution(3, 5)
solution(3, 3)
solution(5, 3)
