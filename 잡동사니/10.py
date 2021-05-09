def solution(code, day, data):
    answer = []
    for i in range(len(data)):
        tmp = data[i].split(' ')
        if tmp[1].replace("code=", '') == code:
            if tmp[2].replace('time=', '')[:8] == day:
                answer.append(data[i])

    answer = sorted(answer, key=lambda x : x.split(' ')[2])
    print(answer)
    ret = []
    for i in answer:
        t = i.split(' ')[0].replace('price=', '')
        ret.append(int(t))

    print(ret)
    return ret

solution("012345", "20190620",
    ["price=80 code=987654 time=2019062113",
    "price=90 code=012345 time=2019062014",
    "price=120 code=987654 time=2019062010",
    "price=110 code=012345 time=2019062009",
    "price=95 code=012345 time=2019062111"])