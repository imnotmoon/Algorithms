def solution(n):
    answer = sorted(str(n), reverse=True)
    answer = ''.join(answer)
    print(answer)

    return answer


solution(118372)
