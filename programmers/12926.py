def solution(s, n):
    answer = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lower_s = s.lower()
    for i in range(len(s)):
        if lower_s[i] == ' ':
            answer += ' '
        else:
            tmp = alphabet[(alphabet.index(lower_s[i])+n) % 26]
            if lower_s[i] != s[i]:
                answer += tmp.upper()
            else:
                answer += tmp
    print(answer)
    return answer


solution("AB", 1)
solution("z", 1)
solution("a B z", 4)
