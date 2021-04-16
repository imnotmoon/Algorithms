def solution(n):
    answer = sorted(str(n), reverse=True)
    answer = ''.join(answer)
    return answer


solution(118372)
