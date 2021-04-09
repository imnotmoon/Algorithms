def solution(s):
    answer = True
    numbers = [str(i) for i in range(10)]
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i not in numbers:
                answer = False
    else:
        answer = False
    return answer


solution("a234")
solution("1234")
