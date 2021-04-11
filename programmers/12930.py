def solution(s):
    answer = ''
    idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            idx = 0
            answer += ' '
            continue
        if idx % 2 == 1:
            answer += s[i].lower()
            idx += 1
        elif idx % 2 == 0:
            answer += s[i].upper()
            idx += 1
    print(answer)
    return answer


solution("show me the money")
