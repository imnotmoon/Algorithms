def solution(participant, completion):
    dic = dict()
    for i in completion:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1

    for i in participant:
        if i not in dic.keys() or dic[i] == 0:
            answer = i
        else:
            dic[i] -= 1
    print(answer)
    return answer


solution(["marina", "josipa", "nikola", "vinko", "filipa"],
         ["josipa", "filipa", "marina", "nikola"])
