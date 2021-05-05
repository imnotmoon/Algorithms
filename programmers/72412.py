def solution(info, query):
    answer = []
    infos, queries = [], []
    for i in info:
        info_arr = i.split(' ')
        tmp = []
        for i in range(0, 4):
            tmp.append(info_arr[i][0])
        tmp.append(int(info_arr[-1]))
        infos.append(tmp)
    for q in query:
        query_arr = q.replace(' and', '').split(' ')
        tmp = []
        for i in range(0, 4):
            tmp.append(query_arr[i][0])
        tmp.append(int(query_arr[-1]))
        queries.append(tmp)
    
    for i in range(len(query)):
        cnt = 0
        for j in range(len(infos)):
            for k in range(len(queries[i][0:-1])):
                if infos[j][k] != queries[i][k] and queries[i][k] != '-':
                    break   # 다음사람
                if k == 3 and infos[j][-1] >= queries[i][-1]:
                    cnt += 1
        answer.append(cnt)
    # print(answer)
    return answer

solution(["java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"], 
    ["java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"])
