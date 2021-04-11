def solution(n):
    answer = [int(str(n)[i]) for i in range(len(str(n))-1, -1, -1)]
    print(answer)
    return answer


solution(12345)
