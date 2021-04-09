def solution(strings, n):
    answer = []
    tmp = sorted(strings, key=lambda x: [x[n], x])
    answer = tmp
    return answer


solution(["sun", "bed", "car"], 1)
solution(["abce", "abcd", "cdx"], 2)
