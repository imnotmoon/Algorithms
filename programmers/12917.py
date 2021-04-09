def solution(s):
    answer = sorted(s, reverse=True)
    return ''.join(answer)


solution("Zbcdefg")
solution("EbcdAefBg")
