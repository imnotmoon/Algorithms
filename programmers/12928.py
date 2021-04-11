def solution(n):
    answer = 0
    div = set()
    for i in range(1, n+1):
        if n % i == 0:
            if i not in div:
                div.add(i)
                answer += i
            if n // i not in div:
                div.add(n//i)
                answer += n//i
    print(answer)
    return answer


solution(12)
solution(5)
solution(2996)
