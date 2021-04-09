def solution(n):
    answer = 0
    i = 0
    while 3**(i+1) <= n:
        i += 1

    text = ""
    while i >= 0:
        div = n // (3**i)
        text += str(div)
        n -= div*(3**i)
        i -= 1
    for j in range(len(text)):
        answer += (3**j)*int(text[j])
    return answer


solution(3)
