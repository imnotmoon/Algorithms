def solution(s):
    answer = []
    temp = []
    s = s[2:-2].split('},{')
    for ss in s:
        temp.append(ss.split(','))
        for j in range(len(temp[-1])):
            temp[-1][j] = int(temp[-1][j])
    temp.sort(key=lambda x : len(x))
    
    answer.append(temp[0][0])
    for i in range(1, len(temp)):
        for j in temp[i]:
            if j not in temp[i-1] : answer.append(j)

    print(answer)
    return(answer)

# solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
# solution("{{20,111},{111}}")
# solution("{{123}}")
# solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")