def solution(n, k, cmd):
    answer = ''
    import copy
    from collections import deque
    table = [i for i in range(n)]
    temp = copy.deepcopy(table)
    trash = deque()

    select = k
    print(temp, select)
    for i in range(len(cmd)):
        if cmd[i][0] == 'D':
            select += int(cmd[i][2:])
            # print(temp, select)
        elif cmd[i][0] == 'U':
            select -= int(cmd[i][2:])
            # print(temp, select)
        elif cmd[i][0] == 'C':
            trash.append({"pos" : select, "data" : temp[select]})
            temp.pop(select)
            if select > len(temp)-1 :
                select -= 1
            # print(temp, select)
        elif cmd[i][0] == 'Z':
            recover = trash.pop()
            if recover["pos"] > len(temp)-1:
                temp.append(recover["data"])
            else :
                temp.insert(recover["pos"], recover["data"])
            if recover["pos"] < select:
                select += 1
            # print(temp, select)

    print(table)
    print(sorted(temp))
    print(select)
    print(trash)

    idx = 0
    temp = sorted(temp)
    for i in range(n):
        if i not in temp:
            answer += 'X'
        else :
            answer += 'O'

    
    print(answer)
    return answer

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
# solution(5, 4, ["U 1", "C", "U 1", "C"])